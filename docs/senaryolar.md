# Senaryolar

## Amac

Bu belge Aromora uygulamasinin temel test ve demo akislarini gosterir. Senaryolar sirayla uygulandiginda rol, veritabani, loglama ve raporlama gereklilikleri kontrol edilebilir.

## Basarili Giris

1. Uygulama `python app.py` komutuyla calistirilir.
2. Tarayicida ana sayfa acilir.
3. `/login` ekranina gidilir.
4. Demo admin bilgileri girilir:
   - E-posta: `admin@aromora.local`
   - Sifre: `Admin12345`
5. Giris basarili olursa ana sayfaya donulur ve admin menusu gorunur.
6. `logs` tablosunda `Giris yapildi` kaydi olusur.

## Yetkisiz Islem Denemesi

1. Giris yapmadan ana sayfada bir urun sepete eklenmeye calisilir.
2. Sistem kullaniciyi login ekranina yonlendirir.
3. Standart musteri hesabiyla giris yapilir.
4. `/admin/items` adresi acilmaya calisilir.
5. Sistem 403 yetkisiz erisim hatasi verir; musteri admin islemlerine erisemez.

## Veri Ekleme, Guncelleme ve Silme

1. Admin olarak giris yapilir.
2. `Admin > Urun Ekle` ekranindan yeni urun bilgileri girilir.
3. Urun listeleme ekraninda yeni urun gorulur.
4. Urun duzenleme ekranindan fiyat veya detay bilgisi degistirilir.
5. Urun silme butonuyla urun silinir.
6. Bu islemlerden sonra admin loglarinda `Urun eklendi`, `Urun guncellendi` ve `Urun silindi` kayitlari gorulur.

## Siparis Akisi

1. Yeni musteri `/register` ekranindan kayit olur.
2. Musteri giris yapar.
3. Ana sayfadan fiyatlandirilmis bir urun sepete eklenir.
4. `/cart` ekraninda siparis olusturulur.
5. Siparis basarili olursa `/payment_success` ekrani acilir.
6. `/orders` ekraninda siparis listelenir.

## Rapor Uretme

1. Musteri olarak giris yapilir.
2. `/reports` ekranina gidilir.
3. Kullanici sadece kendi islem gecmisini gorur.
4. `CSV Indir` butonuyla `kullanici_raporu.csv` indirilir.
5. Admin olarak giris yapilir.
6. `/admin/logs` ekraninda tum kullanicilarin loglari gorulur.
7. Kullanici filtresi secilerek belirli bir kullanicinin loglari listelenir.
8. `CSV Indir` butonuyla `sistem_loglari.csv` indirilir.

## Admin Sifre Degistirme

1. Admin olarak giris yapilir.
2. `/admin/users` ekranina gidilir.
3. Hedef kullanici satirindaki `Sifre` butonuna basilir.
4. Yeni sifre ve tekrar alanlari doldurulur.
5. Kayit sonrasi kullanici yeni sifresiyle giris yapabilir.
6. Admin loglarinda sifre degistirme islemi gorulur.

## Log Olusumu

Asagidaki islemlerden sonra `logs` tablosunda tarih/saatli kayit olusmasi beklenir:

- Kullanici kaydi
- Giris ve cikis
- Sepete urun ekleme/cikarma
- Siparis olusturma
- Profil guncelleme
- Sifre sifirlama
- Admin urun ekleme/guncelleme/silme
- Admin kullanici yetkisi degistirme
- Rapor CSV indirme

## Beklenen Ciktilar

- Ana sayfa urunleri listeler.
- Admin paneli sadece admin kullanicida gorunur.
- Musteri kendi siparislerini ve kendi loglarini gorur.
- Admin tum sistem loglarini filtreleyebilir.
- CSV rapor dosyalari indirilebilir.
