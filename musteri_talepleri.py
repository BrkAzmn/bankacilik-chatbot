import pandas as pd
import random
import os

# Dummy müşteri destek talepleri
customer_queries = [
    "Kredi kartım kayboldu, ne yapmalıyım?",
    "Hesap bakiyemi yanlış görüyorum.",
    "Kredi kartı limitimi nasıl artırırım?",
    "Mobil bankacılık şifremi unuttum, nasıl sıfırlarım?",
    "Havale ücreti neden kesildi?",
    "Ödemem iki kez çekildi, nasıl iade alırım?",
    "Kredi başvurum neden reddedildi?",
    "ATM'de para sıkıştı, nasıl geri alırım?",
    "Dijital bankacılık uygulamanızda bir hata alıyorum.",
    "Kredi kartı borcumu nasıl yapılandırabilirim?"
]

# Bankanın otomatik yanıtları (dummy veriler)
bank_responses = [
    "Kredi kartınızı hemen iptal ettik, yeni kartınızı talep edebilirsiniz.",
    "Hesap bakiyenizi güncellemek için müşteri hizmetlerini arayabilirsiniz.",
    "Kredi kartı limit artışı için başvuru yaptınız mı? Gelirinizi belgelemeniz gerekebilir.",
    "Şifrenizi sıfırlamak için SMS doğrulaması yapmanız gerekmektedir.",
    "Havale ücretleri banka politikalarına göre değişmektedir, detaylar için müşteri temsilcisine danışabilirsiniz.",
    "İkinci kez çekilen ödeme 48 saat içinde iade edilecektir.",
    "Kredi başvurunuzun neden reddedildiğini öğrenmek için müşteri hizmetleriyle iletişime geçin.",
    "ATM'de sıkışan paranız 24 saat içinde hesabınıza iade edilecektir.",
    "Dijital bankacılık uygulamanızı güncelleyerek tekrar deneyin.",
    "Kredi kartı borcunuzu yapılandırmak için banka şubenize başvurabilirsiniz."
]

# Dosya adı
file_path = "dummy_musteri_destek.csv"

# Eğer dosya yoksa oluştur
if not os.path.exists(file_path):
    data = []
    for i in range(1000):
        query = random.choice(customer_queries)
        response = random.choice(bank_responses)
        data.append([i+1, query, response])

    # DataFrame oluştur
    df = pd.DataFrame(data, columns=["ID", "Müşteri Talebi", "Banka Yanıtı"])

    # CSV olarak kaydet
    df.to_csv(file_path, index=False)
    print(f"Dummy müşteri destek verisi başarıyla oluşturuldu: {file_path}")
else:
    print(f"Dosya zaten mevcut: {file_path}. Eğer yeniden oluşturmak istiyorsan, önce silmelisin.")
