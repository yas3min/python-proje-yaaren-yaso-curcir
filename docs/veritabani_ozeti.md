# Veritabani Ozeti

## Amac

Aromora uygulamasinda kullanici, urun, sepet, siparis ve islem kayitlari SQLite veritabaninda saklanir. Veritabani islemleri Flask-SQLAlchemy modelleri uzerinden yurutulur.

## Tablolar

| Tablo | Amac |
| --- | --- |
| `users` | Kayitli musterileri ve admin kullanicilari saklar. |
| `items` | Satisa sunulan parfum urunlerini saklar. |
| `cart` | Kullanicilarin sepetindeki urunleri ve adetleri saklar. |
| `orders` | Olusturulan siparislerin ust bilgisini saklar. |
| `ordered_items` | Siparisteki urun kalemlerini saklar. |
| `logs` | Kullanici islemlerini tarih/saat bilgisiyle saklar. |

## Temel Alanlar

| Tablo | Alan | Aciklama |
| --- | --- | --- |
| `users` | `id` | Birincil anahtar. |
| `users` | `name`, `email`, `phone` | Kullanici iletisim ve kimlik bilgileri. |
| `users` | `password` | Hashlenmis sifre. |
| `users` | `admin` | Kullanicinin admin olup olmadigini belirtir. |
| `users` | `email_confirmed` | E-posta dogrulama durumunu tutar. |
| `items` | `id`, `name`, `price`, `category` | Urun temel bilgileri. |
| `items` | `image`, `details`, `price_id` | Urun gorseli, aciklamasi ve odeme icin fiyat kimligi. |
| `cart` | `uid`, `itemid`, `quantity` | Kullanici, urun ve sepet adedi. |
| `orders` | `uid`, `date`, `status` | Siparisi veren kullanici, tarih ve durum. |
| `ordered_items` | `oid`, `itemid`, `quantity` | Siparisteki urun ve adet bilgisi. |
| `logs` | `user_id`, `action`, `created_at` | Islemi yapan kullanici, islem metni ve tarih/saat. |

## Iliskiler

- `users` 1-N `cart`: Bir kullanicinin birden fazla sepet kalemi olabilir.
- `items` 1-N `cart`: Bir urun farkli kullanicilarin sepetinde bulunabilir.
- `users` 1-N `orders`: Bir kullanicinin birden fazla siparisi olabilir.
- `orders` 1-N `ordered_items`: Bir siparis birden fazla urun kalemi icerir.
- `items` 1-N `ordered_items`: Bir urun farkli siparislerde yer alabilir.
- `users` 1-N `logs`: Bir kullanicinin birden fazla islem kaydi olabilir.

## Baslangic Verisi

Uygulama ilk calistiginda `db.create_all()` ile tablolar olusturulur. `ADMIN_EMAIL` ve `ADMIN_PASSWORD` ortam degiskenleri kullanilarak admin hesabi otomatik eklenir. Urun gorselleri `app/static/uploads` klasorunde tutulur; admin paneliyle yeni urun ve gorsel eklenebilir.

## ER Diyagrami

```text
users 1 --- N cart N --- 1 items
users 1 --- N orders 1 --- N ordered_items N --- 1 items
users 1 --- N logs
```
