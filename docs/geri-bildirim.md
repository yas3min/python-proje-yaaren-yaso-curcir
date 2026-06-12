# Proje Geri Bildirim Dosyası

Bu dosya, proje süreci boyunca aynı repo içinde kullanılacak geri bildirim kaydıdır.
Her aşamada yeni geri bildirimler bu dosyanın altına eklenebilir. Amaç öğrenciye
not vermek değil; projenin eksiklerini, belirsiz noktalarını ve bir sonraki aşamada
neye dikkat edilmesi gerektiğini görünür hâle getirmektir.

---

## Grup ve Repo Bilgisi

- Grup adı: yaaren-yaso-curcir
- Repo adı: python-proje-yaaren-yaso-curcir
- İncelenen aşama: Proje önerisi
- İncelenen dosya: `docs/proje_onerisi.md`
- Son commit zamanı: 2026-04-27 12:07:08 +0300
- Teslim durumu: yapıldı

---

# 1. Geri Bildirim: Proje Önerisi

## Genel İzlenim

Proje fikri genel hatlarıyla anlaşılabiliyor. Öneride özellikle modüler yapı planı, veritabanı kullanımı, ön tanımlı admin hesabı, nesne yönelimli tasarım başlıkları görünür durumda. Buna karşılık en az üç kullanıcı rolü, loglama başlıklarının daha somut hâle getirilmesi gerekiyor.

## Ekip ve Görev Dağılımı

| Üye | Önerideki rol/görev | Beklenen çıktı | Yeterlik durumu | Not |
| --- | --- | --- | --- | --- |
| Aysu Çakır | Backend geliştirme, kullanıcı işlemleri | Giriş/kayıt sistemi, sipariş yönetimi | yeterli | Python/teknik kod katkısı görünüyor. |
| Yasemin Bulut | Veritabanı (SQLite) ve OOP tasarımı | Veritabanı tabloları ve sınıf yapıları | yeterli | Python/teknik kod katkısı görünüyor. |
| Yaren Kapucu | Arayüz tasarımı (HTML/CSS) | web arayüzü | riskli | Görev Python kodlama katkısı açısından belirsiz veya kod dışı görünüyor. |

Not: Yaren Kapucu için görev tanımı Python kodlama katkısı açısından riskli veya kod dışı görünüyor. Her ekip üyesinin teknik bir çıktıya katkı vermesi beklenir.

## Teknik Gerekliliklere Yaklaşım

| Başlık | Durum | Açıklama |
| --- | --- | --- |
| Modüler yapı planı | yeterli | Kodun hangi modüllere ayrılacağı açıklanmalı; varsa dosya/klasör adları somutlaştırılmalı. |
| Veritabanı kullanımı | yeterli | Saklanacak veriler, temel tablolar ve mümkünse ilişkiler açık yazılmalı. |
| En az üç kullanıcı rolü | netleşmeli | Roller yalnızca isim olarak değil, yetki ve işlem farklarıyla belirtilmeli. |
| Ön tanımlı admin hesabı | yeterli | Admin rolünün yanında başlangıç hesabı ve görevleri netleştirilmeli. |
| Nesne yönelimli tasarım | yeterli | Temel sınıf, alt sınıflar ve sorumlulukları açıkça yazılmalı. |
| Loglama | netleşmeli | Hangi işlemlerin hangi bilgilerle kaydedileceği belirtilmeli. |
| Raporlama | yeterli | Kullanıcı ve admin raporlarının kapsamı açıklanmalı. |
| Çalıştırılabilirlik planı | yeterli | Programın nasıl başlatılacağı ve temel kullanım akışı belirtilmeli. |
| Grup büyüklüğüne uygun ileri özellikler | yeterli | Seçilen ileri özelliklerin projede nerede kullanılacağı somutlaştırılmalı. |

Genel teknik geri bildirim:

> En az üç kullanıcı rolü başlığı daha somut örneklerle netleştirilmelidir.; Loglama başlığı daha somut örneklerle netleştirilmelidir.; Bazı ekip üyelerinin Python kodlama katkısı görünmüyor; görev dağılımı teknik katkı içerecek şekilde güncellenmelidir.

## Güçlü Görünen Noktalar

- Proje fikri genel düzeyde anlaşılabiliyor.
- Ekip ve görev dağılımı için bir başlangıç yapılmış.
- Veritabanı kullanımı öneride görünür durumda.
- Admin rolü veya admin hesabı öneride belirtilmiş.
- OOP/sınıf yapısı için bir plan yazılmış.
- Raporlama başlığına değinilmiş.

## Eksik veya Netleşmesi Gereken Noktalar

- En az üç kullanıcı rolü başlığı daha somut örneklerle netleştirilmelidir.
- Loglama başlığı daha somut örneklerle netleştirilmelidir.
- Bazı ekip üyelerinin Python kodlama katkısı görünmüyor; görev dağılımı teknik katkı içerecek şekilde güncellenmelidir.

## Açık Kalan Sorular

1. En az üç kullanıcı rolü hangileri olacak ve her rol hangi işlemleri yapabilecek?
2. Python kodlama katkısı görünmeyen üyeler hangi modül veya teknik çıktıyı geliştirecek?
3. Bir sonraki aşamada bu planın kod yapısına nasıl aktarılacağı netleştirilecek mi?

## Bir Sonraki Aşamaya Kadar Beklenenler

1. İlerleme raporuna geçmeden önce veritabanı, roller, OOP sınıfları, loglama ve raporlama planını uygulanabilir hâle getirin.
2. Görev dağılımında her ekip üyesinin üreteceği Python kodu ve dokümantasyon çıktısını somutlaştırın.

## Kısa Sonuç

- [x] Proje fikri genel olarak anlaşılır; küçük netleştirmelerle ilerleyebilir.
- [ ] Proje fikri var ancak teknik plan belirgin biçimde netleşmeli.
- [ ] Proje önerisi eksik; temel başlıkların yeniden doldurulması gerekiyor.
- [ ] Dosya şablon bırakılmış veya anlamlı teslim yapılmamış.

Son not:

> Bu geri bildirim notlandırma amacı taşımaz. Amaç, ilerleme raporu ve kodlama aşamasına geçmeden önce belirsiz veya eksik kalan noktaları görünür hâle getirmektir.

---

> 
