import os
import openai
import pandas as pd
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# OpenAI API Anahtarını Yükle
openai.api_key = os.getenv("OPENAI_API_KEY")

# Dummy müşteri destek verisini yükle
file_path = "dummy_musteri_destek.csv"

# Dosyanın var olup olmadığını kontrol et
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("Dosya başarıyla yüklendi!")
else:
    print(f"Hata: {file_path} bulunamadı! Önce 'musteri_talepleri.py' dosyasını çalıştır.")

# AI Modeliyle Yanıt Üretme Fonksiyonu (Güncellenmiş API Kullanımı)
def generate_ai_response(user_query):
    try:
        client = openai.OpenAI()  # Yeni OpenAI istemcisi oluştur
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sen bir banka müşteri destek asistanısın. Kibar ve yardımcı ol."},
                {"role": "user", "content": user_query}
            ]
        )
        return response.choices[0].message.content  # Yeni format
    except Exception as e:
        return f"Hata oluştu: {e}"

# Test: Bir müşteri talebine yanıt üret
sample_query = "Kredi kartım kayboldu, ne yapmalıyım?"
ai_response = generate_ai_response(sample_query)
print(f"AI Yanıtı: {ai_response}")
