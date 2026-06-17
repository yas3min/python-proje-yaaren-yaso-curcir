# Aromora

Aromora, parfum urunlerinin listelendigi, sepete eklenip siparis verilebildigi Flask tabanli bir e-ticaret uygulamasidir. Proje; kullanici kaydi, rol bazli yetki kontrolu, urun yonetimi, siparis akisi, veritabani loglari ve CSV raporlari ile Python donem projesi yonergesindeki ana gereklilikleri karsilayacak sekilde duzenlenmistir.

## Kullanilan Teknolojiler

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Flask-Bootstrap
- SQLite
- HTML/CSS, Bootstrap

## Kurulum

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

`.env` dosyasi asagidaki degerleri icermelidir:

```env
SECRET_KEY=your_secret_key_here
DB_URI=sqlite:///test.db
FLASK_APP=app.py
FLASK_DEBUG=1
ADMIN_EMAIL=admin@aromora.local
ADMIN_PASSWORD=Admin12345
```

## Calistirma

```bash
python app.py
```

Yonergede `main.py` beklendigi icin ayni uygulama `python main.py` komutuyla da baslatilabilir. Windows uzerinde `run.bat` dosyasi da uygulamayi baslatir. Uygulama ilk acilista veritabani tablolarini ve varsayilan admin hesabini otomatik olusturur.

## Demo Kullanici Bilgileri

Varsayilan admin hesabi:

- E-posta: `admin@aromora.local`
- Sifre: `Admin12345`

Yeni musteri hesabi `/register` ekranindan olusturulabilir. Ziyaretci rolu giris yapmadan urunleri goruntuleyebilir ve arama yapabilir.

## Kullanici Rolleri

- **Ziyaretci:** Giris yapmadan ana sayfayi, urun detaylarini ve arama sonuclarini gorebilir. Sepete ekleme, siparis ve rapor islemleri yapamaz.
- **Musteri:** Kayitli kullanicidir. Sepete urun ekler/cikarir, siparis olusturur, kendi siparislerini ve kendi islem raporlarini gorur, CSV raporu indirebilir.
- **Admin:** Musteri yetkilerine ek olarak urun ekler/duzenler/siler, kullanicilari listeler, kullanici admin yetkisini veya sifresini degistirir, sistem loglarini gorur ve CSV olarak indirir.

Rol davranislari `app/user_roles.py` icindeki `BaseUserRole`, `VisitorRole`, `CustomerRole` ve `AdminRole` siniflariyla temsil edilir.

## Ornek Kullanim Akisi

1. Ziyaretci ana sayfada urunleri inceler.
2. Kullanici kayit olur veya demo admin hesabi ile giris yapar.
3. Musteri bir urunu sepete ekler ve siparis olusturur.
4. Musteri `Raporlarim` ekraninda kendi loglarini gorur ve CSV indirir.
5. Admin panelinden urun ekler, kullanici yetkisi degistirir veya sistem loglarini inceler.

## Proje Yapisi

```text
app.py                    Uygulama giris noktasi
main.py                   Yonergeye uygun alternatif giris noktasi
requirements.txt          Python bagimliliklari
app/
  __init__.py             Flask uygulamasi ve ana route'lar
  db_models.py            SQLAlchemy veritabani modelleri
  funcs.py                Ortak yardimcilar, loglama ve admin kontrolu
  forms.py                Kullanici formlari
  user_roles.py           OOP rol siniflari ve yetki kurallari
  admin/
    routes.py             Admin paneli route'lari
    forms.py              Admin urun formlari
  templates/              HTML sablonlari
  static/                 CSS ve urun gorselleri
docs/                     Teslim dokumantasyonu
instance/test.db          SQLite veritabani
```

## Secilen Ileri Ozellikler

- **SQLAlchemy ORM:** Tum kalici veriler modeller uzerinden SQLite veritabaninda tutulur.
- **Gorsel arayuz:** Flask, Bootstrap ve HTML sablonlariyla web arayuzu bulunur.
- **Dosya yukleme/cikti:** Admin urun gorseli yukleyebilir; musteri ve admin log raporlarini CSV olarak indirebilir.
- **Admin yonetim paneli:** Admin urunleri ve kullanicilari yonetir, kullanici yetkisini degistirebilir.
- **Zenginlestirilmis loglama:** Temel kullanici islemleri veritabanina yazilir ve rapor ekranlarindan sorgulanabilir.

## Raporlama ve Loglama

`logs` tablosu; giris, kayit, cikis, sepete ekleme/cikarma, siparis olusturma, profil guncelleme, sifre sifirlama, admin urun/kullanici islemleri ve CSV indirme islemlerini tarih/saat bilgisiyle tutar.

- Musteri: `/reports`
- Musteri CSV: `/reports/download`
- Admin sistem loglari: `/admin/logs`
- Admin CSV: `/admin/logs/download`

## Notlar

Uygulamada dosya yollari `os.path` ve Flask `current_app.root_path` ile olusturulur. Bu nedenle yuklenen urun gorselleri proje kokune bagli olarak `app/static/uploads` klasorunde saklanir.
