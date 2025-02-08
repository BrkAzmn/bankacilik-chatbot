🚀 Özellikler
✅ Müşteri Destek Yanıtları: Kullanıcıların sorularını analiz ederek banka işlemleri hakkında bilgilendirici yanıtlar sunar.
✅ Döviz Kuru Bilgilendirme: Güncel USD, EUR, GBP döviz kurlarını anlık olarak sorgular.
✅ Duygu Analizi: Kullanıcıların taleplerini analiz ederek duygu durumunu tahmin eder (mutlu, üzgün, nötr vb.).
✅ Öğrenen Yapı: Kullanıcı geçmişini takip ederek daha kişiselleştirilmiş yanıtlar üretir.
✅ Entegre API Kullanımı: OpenAI API ve Döviz Kuru API'si ile etkileşim sağlar.

🏗️ Teknoloji ve Kurulum
Bu proje aşağıdaki teknolojileri kullanır:
🔹 Backend: FastAPI + Python
🔹 AI Modeli: OpenAI GPT-4
🔹 Veritabanı: Dummy CSV verisiyle çalışmaktadır (MySQL/PostgreSQL entegrasyonu için geliştirilebilir).
🔹 Frontend: React Native (isteğe bağlı mobil uygulama entegrasyonu)

📦 Kurulum
1️⃣ Gereksinimleri yükleyin

bash
Kopyala
Düzenle
pip install -r requirements.txt
2️⃣ Çevresel değişkenleri ayarlayın (.env dosyanızı oluşturun ve API anahtarınızı girin).
3️⃣ API'yi başlatın

bash
Kopyala
Düzenle
uvicorn api:app --reload
4️⃣ Test edin

bash
Kopyala
Düzenle
python test.py
📌 API Endpointleri
GET /chatbot/?user_id={user_id}&query={soru}
🔹 Kullanıcının sorusunu analiz eder ve chatbot yanıtı döndürür.
🌟 Geliştirme Süreci
Bu proje, müşteri destek süreçlerini optimize etmek ve bankacılık sektöründe yapay zeka destekli chatbot sistemlerini geliştirmek amacıyla tasarlanmıştır.

