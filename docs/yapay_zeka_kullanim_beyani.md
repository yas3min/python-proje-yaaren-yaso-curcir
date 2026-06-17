# Yapay Zeka Kullanim Beyani

## Amac

Bu belge, Aromora projesinde yapay zeka araclarindan hangi amaclarla yararlanildigini aciklar. Yapay zeka yardimi, projenin anlasilmadan kopyalanmasi icin degil; kodu duzenleme, eksikleri belirleme, hata ayiklama ve dokumantasyonu netlestirme amaciyla kullanilmistir.

## Kullanilan Araclar

| Arac | Kullanim Amaci |
| --- | --- |
| ChatGPT / Codex | Proje yonergesini analiz etme, eksik gereklilikleri belirleme, Flask kodunda rol/log/rapor yapisini duzenleme, dokumantasyon taslaklarini proje gerceklerine gore doldurma. |

## Kullanim Kapsami

- **Kod:** Rol siniflari, merkezi loglama yardimcisi, kullanici/admin rapor route'lari ve CSV cikti islemleri icin yardim alinmistir.
- **Veritabani tasarimi:** Var olan SQLAlchemy modelleri incelenmis, `logs` tablosunun uygulama akisina baglanmasi planlanmistir.
- **Dokumantasyon:** README, teknik rapor, rol-yetki matrisi, veritabani ozeti ve senaryo belgelerinin proje ile uyumlu hale getirilmesinde yardim alinmistir.
- **Fikir gelistirme:** Ziyaretci, musteri ve admin rollerinin yetki farklari netlestirilmistir.

## Kontrol ve Duzenleme

Yapay zeka ile uretilen kod ve metinler proje yapisina uygun olacak sekilde duzenlenmistir. Eklenen route'lar, modeller ve sablonlar calisma sirasinda kontrol edilmis; veritabani islemleri SQLAlchemy uzerinden ve mevcut Flask mimarisine uygun olarak uygulanmistir.

## Sorumluluk Beyani

Teslim edilen calismanin iceriginden ve sunumda aciklanmasindan proje ekibi sorumludur. Yapay zeka bir yardimci arac olarak kullanilmistir; tasarim kararlarini ve kodun ne yaptigini ekip uyeleri aciklayabilmelidir.
