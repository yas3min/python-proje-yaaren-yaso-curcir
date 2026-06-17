# Proje Onerisi

## Ekip Uyeleri

| Ad Soyad | Ogrenci Numarasi | Projedeki Rol |
| --- | --- | --- |
| Aysu Cakir | 202407105006 | Backend gelistirme ve is mantigi |
| Yasemin Bulut | 202407105078 | Veritabani ve nesne yonelimli tasarim |
| Yaren Kapucu | 202407105059 | Arayuz tasarimi ve dokumantasyon |

## Proje Tanimi

Aromora, kullanicilarin parfum urunlerini internet uzerinden inceleyebildigi, sepete ekleyebildigi ve siparis olusturabildigi bir e-ticaret uygulamasidir. Proje; urunlerin merkezi bir veritabaninda tutulmasini, kullanici rollerinin yetkilere gore ayrilmasini, temel islemlerin loglanmasini ve raporlanmasini hedefler.

## Cozulen Problem

Kucuk olcekli parfum satisi yapan bir isletmenin urunlerini duzenli sekilde listeleyebilmesi, musterilerin siparis akisini takip edebilmesi ve yoneticinin sistem hareketlerini gorebilmesi saglanir. Boylece urun yonetimi, musteri islemleri ve islem gecmisi tek uygulamada toplanir.

## Kullanici Rolleri

- **Ziyaretci:** Urunleri gorur, arama yapar, kayit veya giris ekranina ulasir.
- **Musteri:** Kayit olur, giris yapar, sepete urun ekler/cikarir, siparis olusturur, kendi siparislerini ve islem raporlarini gorur.
- **Admin:** Musteri yetkilerine ek olarak urun ekler/duzenler/siler, kullanicilari yonetir, yetki degistirir ve sistem loglarini raporlar.

## Teknik Yaklasim

Backend Python ve Flask ile gelistirilir. Kalici veriler SQLite veritabaninda Flask-SQLAlchemy modelleriyle saklanir. Oturum yonetimi Flask-Login ile, formlar Flask-WTF ile yurutulur. Arayuz HTML, Bootstrap ve ozel CSS ile hazirlanir.

## Moduler Yapi

- `app/__init__.py`: Ana kullanici akislarini ve route'lari tutar.
- `app/admin/routes.py`: Admin paneli islemlerini tutar.
- `app/db_models.py`: Veritabani modellerini tutar.
- `app/user_roles.py`: Ziyaretci, musteri ve admin rol siniflarini tutar.
- `app/funcs.py`: Ortak yardimci fonksiyonlari, loglama ve admin kontrolunu tutar.
- `app/templates`: HTML sablonlarini tutar.
- `docs`: Teslim dokumantasyonunu tutar.

## Veritabani Plani

Temel tablolar `users`, `items`, `cart`, `orders`, `ordered_items` ve `logs` olarak belirlenmistir. Kullanici-sepet, kullanici-siparis, siparis-urun ve kullanici-log iliskileri veritabani uzerinden takip edilir.

## OOP Tasarimi

Roller `BaseUserRole` temel sinifindan turetilen `VisitorRole`, `CustomerRole` ve `AdminRole` siniflariyla temsil edilir. Her rolun yetkileri ve menu davranisi kendi sinifi icinde tanimlanir. Kullanici modeli `role_profile` ve `can(permission)` yardimcilariyla bu rol siniflarini kullanir.

## Loglama ve Raporlama

Giris, kayit, cikis, sepete ekleme/cikarma, siparis olusturma, profil guncelleme, sifre sifirlama, admin urun/kullanici islemleri ve CSV indirme islemleri `logs` tablosuna yazilir. Musteriler kendi loglarini, admin ise tum sistem loglarini gorebilir ve CSV olarak indirebilir.

## Secilen Ileri Ozellikler

- SQLAlchemy ORM kullanimi
- Flask tabanli gorsel arayuz
- Urun gorseli yukleme
- CSV rapor ciktilari
- Admin yonetim paneli
- Zenginlestirilmis veritabani loglama

## Beklenen Cikti

Calistirilabilir, moduler, veritabani kullanan, uc rol iceren, admin hesabi otomatik olusan, loglama ve raporlama ekranlari bulunan bir Python web uygulamasi teslim edilecektir.
