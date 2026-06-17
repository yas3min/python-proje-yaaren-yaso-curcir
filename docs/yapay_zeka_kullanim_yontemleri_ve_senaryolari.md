# Yapay Zeka Kullanım Yöntemleri ve Senaryoları

Bu belgede, proje sürecinde ChatGPT, Copilot, Gemini, Claude vb. büyük dil modellerinin nasıl kullanılabileceği açıklanmaktadır.

Günümüzde birçok projede aktif olarak kullanılırken, şirketler bütçelerine yapay zeka gideri eklerken, birçok kişi vibe coding ile projeler geliştirirken LLM kullanımını yasaklamak ancak sizlerin güncelden geri kalmanıza sebep olacaktır. Python ve yapay zeka kapsamında dersler verirken, ders notlarımda ve bu dokümanı oluştururken bile LLM ve ajan desteği aldığım bir konumda sizlerden hiç kullanmamanızı istemek bir çelişki olurdu.

Ancak proje, öğrencinin anlamadığı kodları kopyaladığı bir teslim hâline gelmemelidir. Özellikle öğrenme aşamasında görevlerin büyük kısmını doğrudan LLM ile yapmak hem öğrenme sürecinizi baltalar hem de ortaya dağınık, uyumsuz ve birçok açığı bulunan projeler çıkmasına sebep olur. Temel kodlama bilmeden vibe coding ile geliştirilen uygulamaların büyük çoğunluğu mimari hatalar ve güvenlik açıkları barındırmaktadır. Öğrenciden burada beklenen; LLM kullansa bile teslim ettiği her kod parçasını, tasarım kararını ve dokümantasyon içeriğini açıklayabilmesidir.

## 1. Temel İlke

LLM, projede yardımcı araç olarak kullanılabilir; fakat nihai sorumluluk öğrenciye aittir.

Aşağıdaki kullanım kabul edilebilir:

- Kavram açıklaması istemek
- Alternatif çözüm yollarını karşılaştırmak
- Hata mesajını açıklatmak
- Kodun neden çalışmadığını analiz ettirmek
- Yazılan kodu gözden geçirtmek
- README veya teknik rapor taslağı hazırlatmak
- SQL tablo tasarımı hakkında öneri almak
- Test senaryosu üretmek
- Kodun daha modüler hâle getirilmesi için öneri almak

Aşağıdaki kullanım uygun değildir:

- Projenin tamamını LLM'e yazdırmak
- Anlaşılmayan kodu doğrudan teslim etmek
- Hata çıktısını anlamadan yalnızca LLM'in verdiği kodu yapıştırmak
- LLM'in uydurduğu kütüphane, fonksiyon veya komutları kontrol etmeden kullanmak
- Akademik beyana LLM kullanımını yazmamak

## 2. Kullanım Şeması

LLM kullanımında aşağıdaki döngü izlenmelidir:

```text
Problemi tanımla
      ↓
Kendi çözüm fikrini yaz
      ↓
LLM'den açıklama / öneri / kontrol iste
      ↓
Çıktıyı incele ve doğrula
      ↓
Kendi projene uyarlayarak uygula
      ↓
Test et
```

LLM çıktısı doğrudan doğru kabul edilmemelidir. Kod mutlaka çalıştırılmalı, hata durumları test edilmeli ve projedeki gerekliliklerle uyumu kontrol edilmelidir.

Kullanım beyanı için her işlemi tek tek kaydetmeniz beklenmez. Proje tesliminde hangi alanlarda, ne amaçla kullandığınızı genel hatlarıyla belirtmeniz yeterlidir. Örneğin: "veritabanı tasarımı için öneri alındı", "hata mesajları açıklatıldı", "teknik rapor taslağı hazırlatıldı". Ayrıntılar için bkz. [Bölüm 5](#5-ai-kullanım-beyanına-yazılması-gerekenler).

## 3. Önerilen Kullanım Senaryoları

### 3.1. Proje fikrini netleştirme

Kullanılabilir prompt:

```text
Python dönem projesi için [proje fikri] üzerinde çalışıyorum. 
Bu fikrin kullanıcı rolleri, veritabanı tabloları ve raporlama gereksinimleri açısından uygun olup olmadığını değerlendir.
Eksik kalan teknik gereklilikleri belirt.
```

Amaç: proje fikrinin yönergedeki zorunlu gereklilikleri karşılayıp karşılamadığını kontrol etmek.

### 3.2. Kullanıcı rolleri tasarlama

```text
Bu projede admin, standart kullanıcı ve ziyaretçi rolleri olacak.
Her rolün yapabileceği işlemleri tablo hâlinde öner.
Yetkilerin gerçekten farklılaşmasına dikkat et.
```

Amaç: kullanıcı tiplerinin yalnızca isim olarak değil, işlevsel olarak ayrışmasını sağlamak.

### 3.3. Veritabanı tasarımı

```text
Aşağıdaki proje için gerekli veritabanı tablolarını öner.
Tablolar arası ilişkileri açıkla.
Gereksiz karmaşıklık ekleme.

Proje: [proje açıklaması]
```

Amaç: kalıcı veri, ilişkili tablolar ve sorgulanabilir log yapısını planlamak.

### 3.4. Kod hatası analiz etme

```text
Aşağıdaki Python kodunda şu hatayı alıyorum.
Hatanın nedenini açıkla ve yalnızca gerekli düzeltmeyi göster.

Hata:
[hata mesajı]

Kod:
[kod]
```

Amaç: hatayı anlamak; yalnızca çalışan kod almak değil.

### 3.5. Kod gözden geçirme

```text
Aşağıdaki kodu modülerlik, okunabilirlik, hata yönetimi ve OOP kullanımı açısından değerlendir.
Kodun tamamını yeniden yazma; yalnızca sorunları ve gerekli düzeltmeleri belirt.

[kod]
```

Amaç: teslim öncesinde kalite kontrol yapmak.

### 3.6. README hazırlama

```text
Aşağıdaki proje bilgilerine göre README.md taslağı hazırla.
Kurulum, çalıştırma, kullanıcı rolleri, demo kullanıcılar ve klasör yapısı bölümleri olsun.

Proje bilgileri:
[bilgiler]
```

Amaç: değerlendiricinin projeyi çalıştırmasını kolaylaştırmak.

### 3.7. Test senaryosu üretme

```text
Bu proje için başarılı giriş, yetkisiz işlem, veri ekleme, rapor alma ve log oluşumu senaryoları üret.
Her senaryoda beklenen sonucu belirt.
```

Amaç: projenin yalnızca yazılmasını değil, test edilebilir olmasını sağlamak.

### 3.8. Dokümantasyon dosyası doldurma

```text
Aşağıdaki proje bilgilerine göre [dosya adı] dosyasını doldurmama yardım et.
Başlıkları koru, yalnızca içerikleri öner.
Eksik ya da belirsiz kalan kısımları belirt.

Proje bilgileri:
[bilgiler]
```

Amaç: `teknik_rapor.md`, `rol_yetki_matrisi.md`, `veritabani_ozeti.md` gibi zorunlu teslim dosyalarını doğru ve eksiksiz doldurmak. LLM taslağı oluşturabilir; ancak içeriğin projeye gerçekten uygun olduğunu öğrenci doğrulamalıdır.

## 4. LLM Çıktısını Kontrol Etme Kuralları

LLM'den alınan her teknik öneri şu sorularla kontrol edilmelidir:

- Bu öneri proje yönergesindeki hangi gerekliliği karşılıyor?
- Kod gerçekten çalışıyor mu?
- Kullanılan kütüphane gerçekten var mı?
- Kodun ne yaptığını açıklayabiliyor muyum?
- Bu çözüm projeme özgü mü, yoksa genel ve yüzeysel mi?
- Hata durumlarında sistem ne yapıyor?
- Bu katkıyı AI kullanım beyanına yazdım mı?

## 5. AI Kullanım Beyanına Yazılması Gerekenler

LLM kullanıldıysa `docs/ai_kullanim_beyani.md` dosyasında açıkça belirtilmelidir.

Örnek:

```text
Bu projede ChatGPT şu amaçlarla kullanılmıştır:

- Veritabanı tablo yapısı için alternatif öneriler alınmıştır.
- Python hata mesajlarının açıklanması için kullanılmıştır.
- README.md dosyasının ilk taslağı oluşturulmuştur.
- Kodun modülerlik açısından gözden geçirilmesi için destek alınmıştır.

Üretilen kodlar ekip tarafından incelenmiş, projeye uyarlanmış ve test edilmiştir.
```

Bu dosya `ai_kullanim_beyani.md` dosyasının yerine geçmez; onu nasıl dolduracağınızı gösterir. Final tesliminde ikisi de bulunmalıdır.

## 6. Kodlama Ajanları: Codex, Claude Code ve Benzerleri

Sohbet tabanlı LLM'lerin (ChatGPT, Claude.ai vb.) bir adım ötesinde, doğrudan kod tabanıyla çalışabilen **kodlama ajanları** bulunmaktadır. Bu araçlar yalnızca öneri üretmekle kalmaz; terminale erişebilir, dosya oluşturabilir, komut çalıştırabilir ve projenizin içinde gezinerek değişiklik yapabilir.

Öne çıkan örnekler:

- **OpenAI Codex / ChatGPT (kodlama modu):** Dosya okuma, yazma ve terminal komutları çalıştırma yeteneğine sahip ajan modu.
- **Claude Code:** Anthropic'in terminal tabanlı kodlama ajanı. Projenizin klasör yapısını okur, dosyalar arasında gezinir, değişiklik önerir ve uygular. VS Code eklentisi veya terminal üzerinden kullanılır.
- **GitHub Copilot:** Editör içinde satır satır öneri sunar; güncel sürümleri sohbet ve ajan modlarını da destekler.
- **Cursor:** VS Code tabanlı bir editördür; yerleşik ajan modu ile dosyalar arasında bağlam kurarak kod üretir ve düzenler.

### Bu araçlarla ne anlaşılabilir?

Kodlama ajanları, sohbet modellerine kıyasla projenizin bütününü daha iyi kavrar: birden fazla dosyayı aynı anda okuyabilir, hata çıktısını terminalden alabilir ve değişikliklerin etkisini geniş bağlamda değerlendirebilir. Bu özellik onları **anlamak için** güçlü bir araç hâline getirir:

- Yazdığınız kodun neden çalışmadığını açıklatmak
- Bir modülün projenin geri kalanıyla nasıl ilişkilendiğini görmek
- Mimari kararlarınızı sorgulatmak ve alternatiflerini tartışmak
- Hata mesajını bağlamıyla birlikte analiz ettirmek

### Dikkat edilmesi gerekenler

Bu araçlar sohbet modellerinden daha güçlüdür; bu nedenle riskleri de daha büyüktür.

- Ajan öneri sunmakla kalmaz, doğrudan dosya değiştirebilir. Kabul etmeden önce ne değiştiğini okuyun.
- Çalışan kod ile doğru kod aynı şey değildir. Ajan çıktısı test edilmeden ve anlaşılmadan teslim edilmemelidir.
- Her tasarım kararının arkasında siz durmalısınız; sunumda kodu ve kararlarınızı açıklayabilmeniz beklenir.
- Bu araçlarla üretilen içerikler de kullanım beyanında belirtilmelidir.

### Önerilen kullanım biçimi

Ajanı kod yazdırmak için değil, **kodu anlamak ve kararlarınızı test etmek** için kullanın:

```text
Şu an yazdığım [modül adı] şöyle çalışıyor: [açıkla]
Bu tasarımın zayıf noktaları neler olabilir?
Yönergedeki [gereklilik] ile uyumlu mu?
```

```text
Bu hata mesajını alıyorum: [hata]
Hatanın kaynağını ve nedenini açıkla.
Düzeltmeyi sen yapma; nereye bakmam gerektiğini göster.
```

### Git commit yönetimi

Kodlama ajanları commit sürecinde gerçekten işe yarar: hangi dosyaların değiştiğini okuyup değişikliği özetleyen bir commit mesajı önerebilir, ya da mevcut commitlere bakarak projenin genel ilerleme akışını özetleyebilir.

Yararlı kullanım örnekleri:

- Son değişikliklere bakarak anlamlı bir commit mesajı önermesini istemek
- Commit geçmişini okutup ilerleme raporuna özet çıkarmak
- Hangi dosyaların henüz commit edilmediğini ve bunların neden önemli olduğunu açıklatmak

```text
Şu an şu dosyaları değiştirdim: [dosya listesi]
Bu değişiklikler için açıklayıcı bir commit mesajı öner.
```

Dikkat edilmesi gerekenler:

- Commit mesajı ajanın önerisi olsa bile içeriği siz onaylamalısınız; yanlış ya da yanıltıcı bir mesaj commit geçmişini bozar.
- Ajanın "git push" veya "git reset" gibi geri alınamaz komutları doğrudan çalıştırmasına izin vermeyin; bu komutları kendiniz çalıştırın.
- Commit geçmişi değerlendirmede incelenir. "ajan commiti" izlenimi bırakan tek tip, anlamsız mesajlar olumsuz etki yaratabilir.

## 7. Neyi Savunabilmelisiniz?

LLM kullanımı öğrenmeyi desteklediği sürece uygundur. Ancak öğrenci, teslim ettiği kodu ve tasarım kararlarını açıklayamıyorsa bu kullanım kabul edilebilir değildir.

Sunum sırasında her ekip üyesi kendi katkısını, kullandığı kodun ne yaptığını ve neden o şekilde tasarlandığını açıklayabilmelidir.
