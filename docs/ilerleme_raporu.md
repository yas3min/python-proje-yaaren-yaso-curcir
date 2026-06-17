# Ilerleme Raporu

## Tamamlananlar

| Tamamlanan Is | Sorumlu Kisi | Kisa Aciklama |
| --- | --- | --- |
| Flask uygulama iskeleti | Aysu Cakir | Ana route'lar, giris/kayit, sepet ve siparis akisi olusturuldu. |
| Veritabani modelleri | Yasemin Bulut | Kullanici, urun, sepet, siparis, siparis kalemi ve log modelleri tanimlandi. |
| Rol ve yetki yapisi | Yasemin Bulut | Ziyaretci, musteri ve admin rolleri OOP siniflariyla ayrildi. |
| Admin paneli | Aysu Cakir | Urun ve kullanici yonetimi ekranlari hazirlandi. |
| Arayuz | Yaren Kapucu | HTML sablonlari ve CSS ile web arayuzu olusturuldu. |
| Loglama ve raporlama | Aysu Cakir / Yasemin Bulut | Temel islemler veritabani loglarina baglandi, kullanici ve admin rapor ekranlari eklendi. |
| Dokumantasyon | Yaren Kapucu | README ve zorunlu docs dosyalari proje gerceklerine gore tamamlandi. |

## Devam Edenler

| Devam Eden Is | Sorumlu Kisi | Durum |
| --- | --- | --- |
| Canli demo kontrolu | Tum ekip | Bagimliliklar kurulu ortamda uygulama baslatilip son kez denenmelidir. |
| Sunum hazirligi | Tum ekip | Her ekip uyesi kendi sorumlu oldugu bolumu aciklayacak sekilde hazirlanmalidir. |

## Problemler

- Ilk dokumantasyon dosyalarinin bir kismi sablon olarak kalmisti.
- Log tablosu modelde bulunmasina ragmen route'lara bagli degildi.
- Kullanici rolleri baslangicta admin ve standart kullanici olarak ikiye yakin duruyordu.

## Cozumler

- Dokumantasyon dosyalari proje gerceklerine gore yeniden yazildi.
- `record_log` yardimcisi eklendi ve temel islemler loglanir hale getirildi.
- `VisitorRole`, `CustomerRole` ve `AdminRole` siniflari ile uc kullanici tipi acik hale getirildi.

## Sonraki Adimlar

- `pip install -r requirements.txt` sonrasi uygulama `python main.py` veya `python app.py` ile calistirilmalidir.
- Demo sirasinda admin hesabiyla urun ekleme, musteri hesabi ile siparis olusturma ve rapor indirme akisi gosterilmelidir.
