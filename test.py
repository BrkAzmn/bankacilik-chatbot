import openai

# API anahtarını buraya ekle
openai.api_key = "SENIN_API_ANAHTARIN"

# API test etmek için bir fonksiyon yazalım
def test_openai_api():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sen bir banka müşteri destek asistanısın."},
                {"role": "user", "content": "Kredi kartım kayboldu, ne yapmalıyım?"}
            ]
        )
        print("API Yanıtı:", response["choices"][0]["message"]["content"])
    except Exception as e:
        print("Hata:", e)

# Test fonksiyonunu çalıştır
test_openai_api()
