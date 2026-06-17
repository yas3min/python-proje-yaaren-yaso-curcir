# Rol ve Yetki Matrisi

## Amac

Bu belge Aromora uygulamasindaki uc kullanici tipinin hangi islemleri yapabildigini gosterir. Roller kodda `app/user_roles.py` dosyasinda siniflarla temsil edilir.

## Roller

- **Ziyaretci:** Giris yapmamis kullanici.
- **Musteri:** Kayit olup giris yapan standart kullanici.
- **Admin:** Sistem yonetim yetkisi olan kullanici.

## Matris

| Islem | Ziyaretci | Musteri | Admin | Aciklama |
| --- | --- | --- | --- | --- |
| Urunleri goruntuleme | Evet | Evet | Evet | Ana sayfa ve urun detaylari herkese aciktir. |
| Urun arama | Evet | Evet | Evet | Arama sayfasi herkese aciktir. |
| Kayit olma | Evet | Hayir | Hayir | Giris yapmis kullanici tekrar kayit ekranina yonlendirilmez. |
| Giris yapma | Evet | Hayir | Hayir | Oturum acik degilken kullanilir. |
| Sepete urun ekleme | Hayir | Evet | Evet | Giris yapmayan kullanici login ekranina yonlendirilir. |
| Sepetten urun cikarma | Hayir | Evet | Evet | Sadece kendi sepetindeki urunleri etkiler. |
| Siparis olusturma | Hayir | Evet | Evet | Sepette urun varsa siparis olusturulur. |
| Kendi siparislerini goruntuleme | Hayir | Evet | Evet | Kullanici sadece kendi siparislerini gorur. |
| Profil guncelleme | Hayir | Evet | Evet | Ad, telefon, e-posta ve sifre guncellenebilir. |
| Kendi log raporunu goruntuleme | Hayir | Evet | Evet | `/reports` ekranindan erisilir. |
| Kendi log raporunu CSV indirme | Hayir | Evet | Evet | `/reports/download` ile cikti alinir. |
| Urun ekleme | Hayir | Hayir | Evet | Admin panelinde yapilir. |
| Urun duzenleme | Hayir | Hayir | Evet | Admin panelinde yapilir. |
| Urun silme | Hayir | Hayir | Evet | Admin panelinde yapilir. |
| Kullanicilari listeleme | Hayir | Hayir | Evet | Admin panelinde kullanici listesi gorulur. |
| Kullanici yetkisi degistirme | Hayir | Hayir | Evet | Admin, baska kullaniciyi admin yapabilir veya adminligini kaldirabilir. |
| Kullanici sifresi degistirme | Hayir | Hayir | Evet | Admin, kullanici yonetimi ekranindan secilen hesabina yeni sifre atayabilir. |
| Kullanici silme | Hayir | Hayir | Evet | Admin kendi hesabini silemez. |
| Tum sistem loglarini goruntuleme | Hayir | Hayir | Evet | `/admin/logs` ekranindan erisilir. |
| Sistem loglarini CSV indirme | Hayir | Hayir | Evet | `/admin/logs/download` ile cikti alinir. |

## Notlar

Admin rolu musteri islemlerini de yapabilir. Ziyaretci rolu sisteme kayitli bir veritabani kullanicisi degildir; ancak kodda `VisitorRole` sinifiyla temsil edilir ve yetkileri acikca tanimlanir.
