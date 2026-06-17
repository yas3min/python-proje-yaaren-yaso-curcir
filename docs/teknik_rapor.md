# Teknik Rapor

## Proje Ozeti

Aromora, parfum urunlerinin internet uzerinden incelenmesini ve satin alma akisinin basit bir sekilde yurutulmesini saglayan Flask tabanli bir e-ticaret uygulamasidir. Sistem; ziyaretci, musteri ve admin rollerini ayirir. Musteriler urunleri sepete ekleyebilir, siparis olusturabilir ve kendi islem gecmislerini raporlayabilir. Adminler urun ve kullanici yonetimi yapabilir, sistem loglarini inceleyebilir.

## Sistem Mimarisi

Uygulama Flask ile gelistirilmistir. `app.py` uygulamayi baslatir. Ana route'lar `app/__init__.py` dosyasinda, admin paneli route'lari `app/admin/routes.py` dosyasinda yer alir. Veritabani modelleri `app/db_models.py`, rol siniflari `app/user_roles.py`, ortak yardimci fonksiyonlar `app/funcs.py` icindedir. HTML sablonlari `app/templates`, CSS ve urun gorselleri `app/static` altindadir.

## Kullanilan Teknolojiler

- Python ve Flask
- Flask-SQLAlchemy ile ORM tabanli veritabani islemleri
- Flask-Login ile oturum yonetimi
- Flask-WTF ile form dogrulama
- SQLite veritabani
- Bootstrap ve ozel CSS ile web arayuzu

## Kurulum ve Calistirma

1. Sanal ortam olusturulur: `python -m venv .venv`
2. Sanal ortam acilir: `.venv\Scripts\activate`
3. Bagimliliklar kurulur: `pip install -r requirements.txt`
4. `.env` dosyasina `SECRET_KEY`, `DB_URI`, `ADMIN_EMAIL` ve `ADMIN_PASSWORD` degerleri yazilir.
5. Uygulama `python app.py` komutuyla calistirilir.

## Kullanici Rolleri ve Yetkiler

- **Ziyaretci:** Urunleri ve arama sonuclarini gorur, kayit/giris ekranlarina ulasir.
- **Musteri:** Sepet, siparis, profil ve kendi raporlari uzerinde islem yapar.
- **Admin:** Musteri yetkilerine ek olarak urun, kullanici, rol ve sistem logu yonetimi yapar.

Roller `BaseUserRole` temel sinifindan tureyen `VisitorRole`, `CustomerRole` ve `AdminRole` siniflariyla temsil edilir. `User.can(permission)` metodu kullanicinin ilgili yetkiye sahip olup olmadigini kontrol eder.

## Temel Moduller

- `app/db_models.py`: `User`, `Item`, `Cart`, `Order`, `OrderedItem`, `Log` modellerini tutar.
- `app/user_roles.py`: Uc kullanici tipinin OOP rol siniflarini ve izinlerini tutar.
- `app/funcs.py`: Admin kontrolu, e-posta yardimcisi ve `record_log` fonksiyonunu tutar.
- `app/__init__.py`: Ana sayfa, giris, kayit, sepet, siparis, profil ve kullanici raporu route'larini tutar.
- `app/admin/routes.py`: Admin urun, kullanici ve log yonetimi route'larini tutar.

## Veritabani Yapisi

Veriler SQLite veritabaninda SQLAlchemy modelleriyle saklanir. Urun, kullanici, sepet, siparis ve log bilgileri kalicidir. Tablolar arasinda kullanici-sepet, kullanici-siparis, siparis-urun ve kullanici-log iliskileri vardir.

## Islem Kayitlari ve Raporlama

`record_log(user, action)` yardimcisi temel islemleri `logs` tablosuna yazar. Kaydedilen baslica islemler:

- Giris, kayit ve cikis
- Sepete urun ekleme/cikarma
- Siparis olusturma
- Profil guncelleme ve sifre sifirlama
- Admin urun ekleme/guncelleme/silme
- Admin kullanici yetkisi degistirme, sifre degistirme ve kullanici silme
- CSV raporu indirme

Musteriler `/reports` ekraninda kendi loglarini gorur ve `/reports/download` ile CSV indirir. Admin `/admin/logs` ekraninda tum loglari veya belirli kullanici loglarini filtreleyebilir, `/admin/logs/download` ile CSV cikti alabilir.

## Kullanilan Ileri Ozellikler

- SQLAlchemy ORM
- Flask tabanli gorsel arayuz
- Urun gorseli yukleme
- CSV rapor ciktilari
- Admin yonetim paneli
- Zenginlestirilmis veritabani loglama
- OOP rol siniflari ve yetki kontrolu

## Test ve Degerlendirme

Uygulama `python app.py` ile calistirilir. Demo admin hesabi ile giris yapilip urun ekleme, kullanici yetkisi degistirme ve sistem loglarini goruntuleme test edilir. Yeni musteri hesabi olusturulup sepete ekleme, siparis verme ve kullanici raporu indirme senaryolari denenir.

## Karsilasilan Problemler ve Cozumler

Ilk yapida log tablosu bulunmasina ragmen route'lara bagli degildi. Bu nedenle merkezi `record_log` yardimcisi eklendi ve temel islemler bu yardimciyla veritabanina yazildi. Kullanici tipi de sadece admin/musteri ayrimina dayaniyordu; ziyaretci, musteri ve admin rolleri ayri siniflara tasindi.

## Sonuc

Proje moduler yapida, veritabani kullanan, uc rol barindiran, OOP rol siniflari olan, admin hesabi olusturan, loglama ve raporlama yapabilen calisabilir bir e-ticaret uygulamasi haline getirilmistir.
