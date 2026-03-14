# Django Signals (Sinyaller) Örnek Uygulaması

**Geliştirici Bilgileri:**
- **Ad Soyad:** Ali Akbaş
- **Öğrenci No:** 2024481058
- **Üniversite:** Sivas Cumhuriyet Üniversitesi
- **Sınıf:** 2. Sınıf
- **Bölüm:** Bilişim Sistemleri ve Teknolojileri

---

## Projenin Amacı (Ne Yaptık?)

Bu proje, Django framework'ündeki **Signals (Sinyaller)** yapısını anlamak için hazırlanmış küçük bir örnektir.
Veritabanına bir `Makale` (Article) kaydı eklendiğinde, güncellendiğinde veya silindiğinde bu durumu otomatik olarak algılayıp `SistemLog` (Log) tablosuna kayıt düşen bir yapı kurgulanmıştır.

Bunu yapmak için Django'nun dahili `post_save` (kayıt oluşturulduktan sonra) ve `post_delete` (kayıt silindikten sonra) sinyallerini dinleyen fonksiyonlar (`@receiver`) yazılmıştır.

## Önemli Dosyalar

- `blog/models.py`: Burada `Makale` ve logları tutacağımız `SistemLog` veritabanı tablolarımızı tanımladık.
- `blog/signals.py`: Asıl işin döndüğü kısım. Bu dosyada `Makale` modeli üzerinde gerçekleşen olayları (oluşturma/silme) dinleyen ve `SistemLog` modeline yeni kayıt ekleyen fonksiyonlarımız mevcut.
- `blog/apps.py`: Django'nun sinyallerimizi projenin başında görebilmesi için `ready` metodu içerisinde sinyaller dosyamızı içeri (`import`) aktardık.

---

## Nasıl Çalıştırılır?

Bu projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla terminal (veya komut satırı) ortamında uygulayın:

**1. Gerekli kütüphaneleri yükleyin:**
Projede sadece Django kullanılmaktadır. Yüklü değilse şu komutla yükleyin:
```bash
pip install django
```

**2. Proje dizinine terminalden gidin:**
Komut satırınızın şu anda `manage.py` dosyasının bulunduğu `signals ufak örnek` klasöründe (dizininde) olduğuna emin olun.

**3. Veritabanı tablolarını oluşturun (Migration):**
Projeyi ilk defa çalıştırırken veritabanını hazırlamamız gerekiyor:
```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Bir yönetici (Superuser) hesabı oluşturun:**
Admin paneline girip makale oluşturmak için şu komutu girin ve sizden istenen bilgileri (kullanıcı adı, e-posta, şifre vb.) doldurun (şifre yazarken ekranda görünmez, yazıp enter'a basın):
```bash
python manage.py createsuperuser
```

**5. Geliştirici Sunucusunu Başlatın:**
```bash
python manage.py runserver
```

**6. Test Edin (Sinyalleri Gözlemleyin):**
- Tarayıcınızda `http://127.0.0.1:8000/admin` adresine gidin.
- Oluşturduğunuz yönetici hesabı ile giriş yapın.
- **"Makaleler"** kısmına tıklayarak yeni bir makale ekleyin.
- Kaydettikten sonra tekrar admin paneli anasayfasına dönüp **"Sistem Logları"** kısmına girin.
- Harika! Siz sadece bir makale eklediniz ama Django'daki sinyalimiz arka planda çalıştı ve "Sisteme yeni bir makale eklendi..." şeklinde bir logu kendi kendine oluşturdu.
- Aynı zamanda makaleyi güncellediğinizde veya sildiğinizde de otomatik loglamanın çalıştığını görebilirsiniz.
