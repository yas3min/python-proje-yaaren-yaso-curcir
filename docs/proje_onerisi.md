
`[Tam yönergeye göre seçil# Proje Önerisi

## Ekip Üyeleri

| Ad Soyad | Öğrenci Numarası | Projedeki Rol |
| --- | --- | --- |
| Aysu Çakır | 202407105006 | Backend geliştirme ve iş mantığı |
| Yasemin Bulut | 202407105078 | Veritabanı ve nesne yönelimli tasarım |
| Yaren Kapucu | 202407105059 | Arayüz (Frontend) tasarımı |

## Proje Tanımı

Bu proje, kullanıcıların online ortamda parfüm ürünlerini inceleyip satın alabilecekleri bir e-ticaret sistemi geliştirmeyi amaçlamaktadır. Proje kapsamında kullanıcılar hesap oluşturabilecek, ürünleri görüntüleyebilecek, sepete ekleyebilecek ve sipariş oluşturabilecektir. Sistem ayrıca admin paneli ile ürün yönetimini desteklemektedir.

## Görev Dağılımı

| Ad Soyad | Sorumlu Olduğu Bölüm veya Görev | Beklenen Çıktı |
| --- | --- | --- |
| Aysu Çakır | Backend geliştirme, kullanıcı işlemleri | Giriş/kayıt sistemi, sipariş yönetimi |
| Yasemin Bulut | Veritabanı (SQLite) ve OOP tasarımı | Veritabanı tabloları ve sınıf yapıları |
| Yaren Kapucu | Arayüz tasarımı (HTML/CSS) |  web arayüzü |

## Gerekliliklere Yaklaşım
Proje, frontend ve backend yapısının birlikte çalışması üzerine tasarlanmıştır. Backend tarafında Python ve Flask framework’ü kullanılacaktır. Kullanıcıdan alınan veriler backend tarafında işlenerek SQLite veritabanına kaydedilecektir. Kod yapısı modüllere ayrılarak düzenli ve okunabilir hale getirilecektir. Kullanıcı, ürün ve sipariş işlemleri ayrı fonksiyonlar ve sınıflar üzerinden yönetilecektir.

### Genel Proje Çalışma Sistemi

Kullanıcılar sisteme kayıt olarak giriş yapar. Giriş yaptıktan sonra ürünleri listeleyebilir, ürün detaylarını inceleyebilir ve sepete ekleyebilirler. Sepet üzerinden sipariş oluşturulabilir. Admin kullanıcı ise sisteme giriş yaparak ürün ekleme, silme ve güncelleme işlemlerini gerçekleştirebilir.

### Modüler Yapı ve Kod Kalitesi

Proje, farklı modüllere ayrılarak geliştirilecektir. Kullanıcı işlemleri, ürün işlemleri ve sipariş işlemleri ayrı modüllerde yer alacaktır. Tekrar eden kodlar fonksiyonlara ayrılacak ve anlamlı isimlendirme yapılacaktır. Kod içerisinde gerekli yerlerde açıklayıcı yorum satırları kullanılacaktır.

### Veritabanı Kullanımı

Projede kullanıcı bilgileri, ürünler ve siparişler veritabanında saklanacaktır. Kullanılacak temel tablolar şunlardır: Users, Products, Orders. Veritabanı olarak SQLite tercih edilecektir.

### Kullanıcı Yönetimi ve Yetkiler

Sistemde iki tür kullanıcı bulunmaktadır: Normal kullanıcı: Ürünleri görüntüler, sepete ekler ve sipariş oluşturur
Admin kullanıcı: ürün ekleme, silme ve güncelleme işlemlerini yapar ,Admin tüm kullanıcı işlemlerini görüntüleyebilir.

### Nesne Yönelimli Tasarım

Projede nesne yönelimli programlama yaklaşımı kullanılacaktır. Temel sınıflar şunlardır:User, Product, Cart, Order.
Bu sınıflar sistemdeki temel işlemleri gerçekleştirmek için kullanılacaktır.

### Loglama ve Raporlama

Sistemde temel kullanıcı işlemleri (giriş ve sipariş işlemleri) kayıt altına alınacaktır. Bu kayıtlar tarih ve saat bilgisi ile saklanacaktır. Kullanıcılar kendi geçmiş siparişlerini görüntüleyebilecektir.

### Seçilen İleri Özellikler
Kullanıcılar seçtikleri ürünlerin detay bilgilerine (marka, isim, fiyat) erişebilmektedir ,dinamik sepet yapısı sayesinde kullanıcılar ürünleri sepete ekleyebilmekte ve anlık olarak sepet içeriklerini görüntüleyebilmektedir ,Kullanıcı oturum yönetimi ile her kullanıcıya özel sepet yapısı oluşturulmuştur.
