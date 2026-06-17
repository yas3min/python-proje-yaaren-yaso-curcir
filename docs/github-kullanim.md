# Git ve GitHub Kullanım Kılavuzu

Bu dosya, ders projesi kapsamında Git ve GitHub kullanımını açıklamak için hazırlanmıştır.

---

## Genel Açıklama

### Git nedir?

Git, yazılım geliştirme sürecinde dosya değişikliklerini takip etmek için kullanılan bir **versiyon kontrol sistemidir**. Bu tip projelerde daha önceden yapılan değişikliklerin kaybolmaması için dosyaların son halleri "proje_son", "proje_son_1", "proje_son_2", "proje_bu_sefer_gercekten_son", "proje_bu_sefer_gercekten_son_2" gibi yeni isimlerle tutulabilmekte, bu da çok fazla karmaşaya sebep olmaktadır. Git sistemi bu süreci otomatik olarak yönetir. Projenizde bir değişiklik yaptığınızda bunu `commit` komutuyla kaydettiğinizde o versiyon saklanır; istenirse eski versiyona dönülebilir veya versiyonlar arasındaki farklara bakılabilir. Ayrıca bu sistem çok kullanıcının ortak dosyalarda çalışmasını da yönetir.

Temel kavramlar:

- **commit**: yapılan değişikliğin kaydı
- **repository (repo)**: projenin bulunduğu klasör
- **branch**: paralel geliştirme hattı
- **pull / push**: uzaktaki repo ile veri alışverişi

---

### GitHub nedir?

Git tek başına yerel bir araçtır; dosyalarınızı bilgisayarınızda takip eder, ancak başka biriyle çalışmak için onun bilgisayarına doğrudan bağlanmanız gerekir. Bunu klasik yöntemle yapmanın yolu — değişiklikleri zip'leyip göndermek, ortak bir ağ sürücüsü kurmak ya da her push işlemi için karşı tarafın bilgisayarına SSH ile bağlanmak — hem yavaş hem de hata yapmaya açıktır.

**GitHub**, bu problemi çözmek için Git repolarını internet üzerinde barındıran bir platformdur. Herkes değişikliklerini GitHub'daki ortak repoya gönderir (`push`), ortak repodan çeker (`pull`); böylece ekip çalışması merkezi ve takip edilebilir hâle gelir. Bugün yazılım sektöründe neredeyse her şirket kaynak kodunu bu modelle yönetmektedir: açık kaynak projeler, şirket içi ürünler, araştırma kodları. GitHub, dünya genelinde 100 milyondan fazla geliştiricinin kullandığı, sektörün fiili standardı olan platformdur.

**GitHub Classroom**, GitHub'ın eğitim kurumlarına sunduğu ek bir katmandır. Eğitmenler bir "classroom" oluşturur ve ödev (assignment) hazırlar; her öğrenci veya grup için otomatik olarak ayrı bir repo oluşturulur. Eğitmen bu repolara erişebilir, commit geçmişini görebilir ve isteğe bağlı olarak otomatik test sonuçlarını takip edebilir. Teslim e-postayla ya da dosya göndererek değil, bu repoya yapılan son `push` ile gerçekleşir.

---

### GitHub Classroom nasıl çalışır?

Eğitmen bir assignment hazırladığında size bir **davet linki** gönderir. Bu linke girip "Accept assignment" dediğinizde GitHub Classroom sizin için özel bir repo oluşturur. O andan itibaren yapmanız gereken tek şey bu repoyu bilgisayarınıza clone'layıp çalışmak ve değişiklikleri düzenli olarak push'lamaktır.

- Her ödev için size özel bir repo oluşturulur.
- Bu repo sizin **tek teslim yerinizdir**; e-posta veya başka yöntemlerle teslim kabul edilmez.
- Tüm değişiklikler commit geçmişiyle birlikte değerlendirilir; son commit zamanı teslim zamanı olarak alınır.

---

## Zorunlu Dosya Yapısı

Bu derste teslimler aşağıdaki klasör yapısı üzerinden yapılacaktır. Dosyaların doğru konumda olması zorunludur; yanlış konuma yüklenen dosyalar değerlendirilmez.

```text
docs/proje_onerisi.md
docs/ilerleme_raporu.md
docs/teknik_rapor.md
docs/rol_yetki_matrisi.md
docs/veritabani_ozeti.md
docs/senaryolar.md
docs/ai_kullanim_beyani.md
```

Şablonda `data/`, `logs/` ve `outputs/` klasörlerinin içinde `.gitkeep` adlı boş dosyalar bulunmaktadır. Git, içi boş klasörleri takip edemediğinden bu dosyalar klasörün repoda görünmesini sağlamak için konulmuştur. Bu klasörlere kendi dosyalarınızı eklediğinizde `.gitkeep` dosyaları işlevini tamamlar; silebilir ya da olduğu gibi bırakabilirsiniz.

---

## Talimatlar

Git sistemi terminal üzerinden, kendi uygulaması ile, VS Code gibi editör/IDE eklentileri üzerinden veya GitHub Desktop, GitKraken gibi uygulamalar üzerinden kontrol edilebilmektedir. Tavsiye edilen yol VS Code veya GitHub Desktop uygulamasıdır. Aşağıda öncelikle terminal üzerinden temel komutlar verilecektir. Eklenti veya arayüz kullansanız bile temel komutları en azından bir kere deneyip uygulamanızda fayda vardır.

### Git kurulumu

Git sisteminin bilgisayarınızda kurulu olması gerekmektedir. Bazı sistemlerde varsayılan olarak kurulu olabilir. Git kurulu olup olmadığını kontrol edin:

```bash
git --version
```

Kurulu değilse: [https://git-scm.com](https://git-scm.com)

Git'i ilk kez kullanıyorsanız kimliğinizi tanımlayın (bunu bir kez yapmanız yeterlidir):

```bash
git config --global user.name "Ad Soyad"
git config --global user.email "eposta@ornek.com"
```

---

### GitHub kullanımı

#### 1. Assignment'ı kabul edin

1. GitHub Classroom linkine girin.
2. "Accept assignment" butonuna tıklayın.
3. Size özel repo oluşturulmasını bekleyin.

#### 2. Repo linkini kopyalayın

GitHub sayfasında "Code" butonuna basın ve HTTPS bağlantısını kopyalayın.

#### 3. Repoyu bilgisayarınıza indirin

```bash
git clone <repo_linki>
cd <repo_adi>
```

#### 4. Çalışmanızı kaydedin

Değişiklikleri takibe alın ve commit edin:

```bash
git add .
git commit -m "Açıklayıcı bir mesaj yazın"
```

#### 5. GitHub'a gönderin

```bash
git push origin main
```

> Bu derste tüm repolarda ana branch adı `main` olarak kullanılacaktır.

#### 6. Kontrol edin

GitHub sayfasına giderek dosyaların yüklendiğini ve commit geçmişini doğrulayın.

---

### Linux, Windows ve macOS'ta bağlanmak

Üç platformda da temel komutlar aynıdır. Farklılıklar yalnızca terminale nasıl ulaşıldığında ortaya çıkar:

| Platform | Terminal                                         |
| -------- | ------------------------------------------------ |
| Linux    | Terminal uygulaması                              |
| macOS    | Terminal veya iTerm2                             |
| Windows  | Git Bash (Git kurulumunla gelir) veya PowerShell |

Windows'ta Git Bash kullanmanız önerilir; böylece Linux/macOS ile aynı komutları kullanabilirsiniz.

#### GitHub kimlik doğrulaması (HTTPS)

İlk push sırasında GitHub sizden giriş yapmanızı isteyecektir. Tarayıcı üzerinden GitHub hesabınızla oturum açarak işlemi tamamlayabilirsiniz.

Terminal kullanıyorsanız ve tarayıcı açılmıyorsa GitHub **kişisel erişim tokeni (PAT)** ile giriş yapılması gerekebilir. Token oluşturmak için:

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token" butonuna tıklayın, `repo` iznini seçin.
3. Oluşturulan tokeni kopyalayın; push sırasında parola yerine bu tokeni girin.

Tokeni tekrar tekrar girmemek için:

```bash
git config --global credential.helper store
```

---

### VS Code ile bağlanmak

VS Code, Git entegrasyonunu yerleşik olarak sunar; terminal kullanmak zorunda kalmazsınız. Proje için tavsiye edilen yöntem budur.

#### Repo'yu VS Code ile açmak

1. VS Code'u açın.
2. "Clone Git Repository" seçeneğiyle repo linkini yapıştırın.
3. Yerel klasörü seçin; VS Code otomatik olarak clone işlemini tamamlar.

#### Değişiklik kaydetmek (commit ve push)

1. Sol panelde **Source Control** simgesine tıklayın (Ctrl+Shift+G).
2. Değiştirilen dosyaların yanındaki **+** simgesiyle onları stage'e alın.
3. Üstteki mesaj kutusuna açıklama yazın ve **Commit** butonuna tıklayın.
4. "Sync Changes" veya **Push** butonuyla değişiklikleri GitHub'a gönderin.

> İlk push işleminde VS Code sizden GitHub hesabınızla oturum açmanızı isteyebilir.

---

### GitHub Desktop ile bağlanmak

GitHub Desktop, terminal veya VS Code yerine Git işlemlerini tamamen görsel bir arayüzle yapmanızı sağlayan resmi bir uygulamadır. İndirmek için: [desktop.github.com](https://desktop.github.com)

#### Kurulum ve giriş

1. GitHub Desktop'ı indirip kurun.
2. Uygulamayı açın ve GitHub hesabınızla oturum açın (File → Options → Accounts).

#### Repoyu bilgisayarınıza indirin (clone)

1. Üst menüden **File → Clone repository** seçin.
2. "URL" sekmesine geçip GitHub Classroom repo linkini yapıştırın.
3. Yerel klasörü seçin ve **Clone** butonuna tıklayın.

#### Commit ve push işlemi

1. Yaptığınız değişiklikler sol panelde otomatik olarak listelenir.
2. Dahil etmek istediğiniz dosyaları işaretleyin.
3. Sol alttaki **Summary** kutusuna kısa bir açıklama yazın ve **Commit to main** butonuna tıklayın.
4. Üst menüdeki **Push origin** butonuyla değişiklikleri GitHub'a gönderin.

> Commit yaptıktan sonra Push origin butonu belirene kadar değişiklikler yalnızca bilgisayarınızda saklanır; GitHub'a gönderilmez.

---

## Çalışma Disiplini

- Büyük değişiklikleri tek commit yerine küçük parçalara bölün.
- Anlamlı commit mesajları yazın; "güncelleme" veya "değişiklik" gibi belirsiz mesajlardan kaçının.
- Yalnızca son gün değil, süreç boyunca düzenli commit atın; commit geçmişi değerlendirmede dikkate alınır.

---

## Sık yapılan hatalar

- Değişikliği yapıp **push yapmamak** — commit tek başına yetmez.
- Yanlış repoya yükleme yapmak.
- Assignment'ı accept etmeden işlem yapmaya çalışmak.
- Grup reposu yerine bireysel repo kullanmak.
- Son dakika yükleme — push işleminin tamamlanması zaman alabilir.

---

## Öneriler

### Araç seçimi

Hangi aracı kullanacağınızdan emin değilseniz şu sırayı izleyin:

- **Başlangıç için:** GitHub Desktop — kurulumu basit, her adım görünür, hata yapma ihtimaliniz düşük.
- **Kod yazarken:** VS Code yerleşik Git paneli — editörden çıkmadan commit ve push yapabilirsiniz.
- **Terminal:** Temel komutları en az bir kez çalıştırın; araçların arka planda ne yaptığını anlamak için önemlidir.

İlerleyen haftalarda VS Code'a geçmek daha verimli olacaktır; GitHub Desktop iyi bir başlangıç noktasıdır.

---

### Grup çalışmasında iş akışı

Aynı repo üzerinde birden fazla kişi çalışırken çakışmaları önlemek için birkaç basit kurala uymak yeterlidir:

- Çalışmaya başlamadan önce her zaman `git pull` yapın; böylece takım arkadaşlarınızın son değişikliklerini alırsınız.
- Mümkünse aynı anda aynı dosyayı düzenlemeyin; görev dağılımını modül bazında yapın.
- Her anlamlı iş parçasını bitirince push edin; günlerce yerel tutmayın.
- Commit mesajına kimin ne yaptığını değil, ne değiştiğini yazın — Git zaten kimin yaptığını kaydeder.

---

### İyi commit mesajı nasıl yazılır?

Commit mesajı, o değişikliği ileride sizin veya takım arkadaşınızın anlayabilmesi için yazılır.

**Kaçınılması gerekenler:**

```text
güncelleme
değişiklik yaptım
düzeltme
aaa
son hali
```

**Bunlar yerine:**

```text
kullanici girisi icin login fonksiyonu eklendi
veritabani baglanti hatasi giderildi
rol yetki matrisi guncellendi
admin rapor ekrani tamamlandi
```

Kısa ve fiil cümlesi biçiminde yazmak yeterlidir. Türkçe veya İngilizce olabilir; önemli olan tutarlı olmaktır.

## Teslim kuralı

- Teslim yalnızca GitHub Classroom üzerinden yapılır.
- Son commit zamanı esas alınır.
- Commit edilmiş ancak push edilmemiş değişiklikler teslim sayılmaz.
- Repo'da görünmeyen dosyalar teslim edilmemiş sayılır.
