from fastapi import FastAPI
import openai
import os
import requests
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware - React ile bağlantı için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# .env dosyasını yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Kullanıcı konuşma geçmişini saklamak için bellek
chat_history = {}

# Döviz Kuru API'si (ExchangeRate API)
def get_exchange_rate(currency_code):
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")  # USD bazlı veri çekiyoruz
        data = response.json()
        if "TRY" in data["rates"]:
            usd_to_try = data["rates"]["TRY"]  # 1 USD kaç TRY?
            if currency_code == "USD":
                return round(usd_to_try, 2)  # 1 USD = X TL
            elif currency_code in data["rates"]:
                rate = data["rates"][currency_code]
                return round(usd_to_try / rate, 2)  # Diğer kurları TL'ye çevir
            else:
                return "Bu para birimi bulunamadı."
        else:
            return "Döviz kuru bilgisi alınamadı."
    except Exception as e:
        return f"Döviz kuru alınamadı: {e}"

@app.get("/chatbot/")
def chatbot_response(user_id: str, query: str):
    try:
        # Eğer kullanıcı daha önce konuşmadıysa, yeni bir liste başlat
        if user_id not in chat_history:
            chat_history[user_id] = []

        # Döviz kuru isteği mi kontrol et
        if "dolar" in query.lower():
            usd_rate = get_exchange_rate("USD")
            return {"response": f"Bugün 1 Dolar = {usd_rate} TL", "emotion": "Bilgi"}
        elif "euro" in query.lower():
            eur_rate = get_exchange_rate("EUR")
            return {"response": f"Bugün 1 Euro = {eur_rate} TL", "emotion": "Bilgi"}
        elif "sterlin" in query.lower():
            gbp_rate = get_exchange_rate("GBP")
            return {"response": f"Bugün 1 Sterlin = {gbp_rate} TL", "emotion": "Bilgi"}

        # OpenAI API ile duygu analizi yapalım
        emotion_analysis_prompt = f"Aşağıdaki cümlenin duygu analizini yap:\n\n'{query}'\n\nDuygu: (Mutlu, Üzgün, Kızgın, Nötr, Heyecanlı)"
        
        client = openai.OpenAI()
        emotion_response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Sen bir duygu analiz asistanısın."},
                      {"role": "user", "content": emotion_analysis_prompt}]
        )

        emotion = emotion_response.choices[0].message.content.strip()

        # Chatbot yanıtı oluştur
        messages = [{"role": "system", "content": "Sen bir banka müşteri destek asistanısın. Kullanıcıya yalnızca resmi bir dil kullanarak yardımcı ol. Kibar, profesyonel ve net bir şekilde yanıt ver."}]
        messages.extend(chat_history[user_id])
        messages.append({"role": "user", "content": query})

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )

        ai_response = response.choices[0].message.content

        # Konuşma geçmişine ekle
        chat_history[user_id].append({"role": "user", "content": query})
        chat_history[user_id].append({"role": "assistant", "content": ai_response})

        # Hafıza boyutunu sınırla (Son 20 mesajı sakla)
        if len(chat_history[user_id]) > 20:
            chat_history[user_id] = chat_history[user_id][-20:]

        return {"response": ai_response, "emotion": emotion}
    
    except Exception as e:
        return {"error": str(e)}

# API çalıştırma komutu:
# uvicorn api:app --reload