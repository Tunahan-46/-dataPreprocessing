📊 Makine Öğrenmesi ile Gelir Tahmini ve Veri Önişleme
Bu proje, yapılandırılmamış finansal verilerin temizlenmesi, özellik mühendisliği (feature engineering) ve regresyon modelleri (Doğrusal ve Topluluk Öğrenmesi) kullanılarak gelir tahmini yapılmasını kapsayan bir veri bilimi çalışmasıdır.

📂 Proje Yapısı ve Dosyalar
veri_ile.py: Ham veri setindeki eksik değerlerin (NaN) ortalama ile doldurulması, gereksiz sütunların (ID) kaldırılması ve verilerin gelir düzeyine göre (Düşük, Orta, Yüksek) kategorize edilmesini sağlar.

gelir_tahmin.py: Scikit-learn kütüphanesi kullanılarak oluşturulmuş temel bir LinearRegression modelidir. Yaş ve meslek değişkenleri üzerinden tahmin üretir.

gelişmiş_veri_önişleme.py: Projenin en kapsamlı kısmıdır. Verilerin standartlaştırılması (StandardScaler), RandomForestRegressor kullanımı ve model başarı oranlarının (Accuracy) karşılaştırılmasını içerir.

🛠️ Kullanılan Teknolojiler ve Kütüphaneler
Python 3.x

Pandas: Veri manipülasyonu ve Excel veri okuma/yazma işlemleri.

Scikit-Learn:

LabelEncoder: Kategorik metin verilerini sayısal verilere dönüştürme.

StandardScaler: Özellik ölçeklendirme ile model performansını artırma.

LinearRegression & RandomForestRegressor: Tahmin modelleri.

Openpyxl: Excel dosyalarıyla etkileşim için.

🚀 Kurulum ve Çalıştırma
Gerekli kütüphaneleri yükleyin:

Bash
pip install pandas scikit-learn openpyxl
Veri setini hazırlayın:
veri_on_isleme_ve_ozellik_muhendisligi.xlsx dosyasının proje ana dizininde olduğundan emin olun.

Modeli test edin:
Gelişmiş tahmin sonuçlarını görmek için terminale şunu yazın:

Bash
python gelişmiş_veri_önişleme.py
📈 Model Karşılaştırması
Proje içerisinde iki farklı modelin doğruluk oranları karşılaştırılmaktadır:

Linear Regression: Basit ve hızlı tahminler için.

Random Forest Regressor: Daha karmaşık veri yapıları ve yüksek doğruluk oranı için.
