# Curiosity Shorts Kit kullanım kılavuzu

Bu kılavuz, tek bir brief vererek konu araştırması, hook, seslendirme, sahne planı, görsel arama, gerektiğinde AI promptları ve edit hazırlığını birlikte üretmek içindir. Skill, hazırlık sürecini yürütür; bitmiş videoyu varsayılan olarak oluşturmaz.

## İçindekiler

1. İlk kurulum ve GitHub'a yükleme
2. Skill'i çağırma ve ilk test
3. Briefte hangi bilgileri vermelisin
4. Kopyalanabilir kısa brief
5. Kopyalanabilir gelişmiş brief
6. Tek görsel üzerinden test
7. Üç konu alanı için başlangıç örnekleri
8. Sonuçta ne teslim alacaksın
9. Revizyon ve gerçek ses süresine uyarlama
10. Görsel bulunamadığında ve araçlar eksik olduğunda
11. İlk testleri değerlendirme
12. Sık karşılaşılan sorunlar
13. Dosyaların görevleri ve resmî kaynaklar

## 1 İlk kurulum ve GitHub'a yükleme

### ZIP'i aç ve doğru klasörü yükle

Arşivi açınca `curiosity-shorts-kit` klasörünü göreceksin. Bu klasörün **içeriğini** kendi GitHub reponun köküne yükle. Böylece repoda şu yollar bulunur:

- `README.md`
- `START.md`
- `plugin.json`
- `skills/create-curiosity-shorts/SKILL.md`
- `docs/KULLANIM_KILAVUZU.md`
- `tests/scenarios.md`

`skills/create-curiosity-shorts` yolunun önüne yanlışlıkla ikinci bir `curiosity-shorts-kit` klasörü koyarsan kurulumda verdiğin yolu da buna göre değiştirmek gerekir. En kolay yol, README'nin doğrudan repo ana sayfasında görünmesidir.

Yeni ve boş GitHub reposuna terminalden yüklemek istersen, Terminal'de önce açtığın klasöre gir. Ardından aşağıdaki komutları kullan. GitHub adresindeki örnek alanları kendi adresinle değiştir. Bu örnek, mevcut geçmişi olan bir repoyu birleştirme talimatı değildir.

```bash
git init
git add .
git commit -m "Add curiosity Shorts production workflow"
git branch -M main
git remote add origin https://github.com/KULLANICI/REPO.git
git push -u origin main
```

GitHub'ın kimlik doğrulama adımını tamamlaman gerekebilir. Mevcut repoya ekliyorsan onun normal commit/push akışını kullan; yeniden remote ekleme veya geçmişi zorla değiştirme.

### Mac uygulamasında kur

Resmî ChatGPT masaüstü uygulamasına mevcut ChatGPT hesabınla giriş yap. Skill kurulumunu, kullanılabilir olduğu ortamda Codex tarafındaki **Skill Installer** üzerinden yap. CLI veya IDE kullanıyorsan `$skill-installer` çağrısı kullanılabilir. Menü ve özellik erişimi sürümüne ve hesabına göre değişebilir.

Installer'a verilecek mesaj:

```text
Bu GitHub deposundaki skill'i kur:

Repo: https://github.com/KULLANICI/REPO
Skill klasörü: skills/create-curiosity-shorts

Kurulumdan sonra skill adını ve nereden çağırabileceğimi belirt.
Dosyaları okuyamıyorsan kurulmuş gibi davranma; eksik erişimi açıkla.
```

Özel repo için GitHub erişimi gerekebilir. Sadece normal sohbet ekranına adres yapıştırmak kalıcı kurulum değildir. Kurulumdan sonra skill seçicide göründüğünü kontrol et; görünmüyorsa Codex'i yeniden başlatıp kontrol et.

### Webde kullanma ile yerel kurulumu ayır

Yerel skill kurulumu webdeki ChatGPT ortamına otomatik kurulum yapmaz. Pakette plugin manifestleri de bulunur, fakat bu dosyalar plugin'in dizine gönderildiği veya onaylandığı anlamına gelmez. Web dağıtımı için resmî plugin yolu ayrıca izlenir.

Kurulum olmadan hızlı deneme için `START.md` mesajını kullanabilirsin. Modelin hem `SKILL.md` hem gerekli referansları okuyabilmesi gerekir. Erişim yoksa ZIP'i veya gerekli metinleri konuşmaya ekleyebilirsin; bu yöntem o konuşmada talimat kullanımıdır.

## 2 Skill'i çağırma ve ilk test

ChatGPT'de mevcutsa `@` seçicisinden skill'i seç. Codex CLI veya IDE'de `$create-curiosity-shorts` kullan. Görünen başlığı **Merak Shorts Üretimi**, teknik adı **create-curiosity-shorts**.

İlk denemede kısa ve kolay gösterilebilir bir soru seç. İlk mesajda bütün üretim tercihlerini kusursuz doldurman gerekmez. Akış, rutin kararları kendi alıp belirttiği varsayımlarla ilerler.

Örnek çağrı:

```text
$create-curiosity-shorts

Konu: Narvalın uzun çıkıntısı boynuz mu, diş mi?
Seslendirme İngilizce, üretim açıklamaları Türkçe olsun.
Hedef: yaklaşık 30 saniyelik bir Short.
Kendi çekimim yok. Gerçek görüntüler öncelikli.
Bu video için yeni satın alma yok. AI video zorunlu değil.
Tüm aşamaları sırayla tamamlayıp nihai üretim paketini ver.
```

Buradaki `$` çağrısı CLI/IDE içindir. ChatGPT'de skill'i seçtiysen briefin kendisini yazman yeterlidir.

## 3 Briefte hangi bilgileri vermelisin

| Alan | Ne yazmalısın | Örnek |
|---|---|---|
| Konu veya soru | Tek açıklama hedefi | Fermuar sürgüsü iki tarafı nasıl birleştiriyor? |
| Dil ve izleyici | Seslendirme ile üretim notlarını ayırabilirsin | İngilizce ses, Türkçe edit notları; genel izleyici |
| Süre | Hedef veya esnek aralık | 30–40 saniye; zorunlu olmayan bilgiler çıkarılabilir |
| Görsel yaklaşım | Gerçek görüntü, fotoğraf, şema ve AI tercihleri | Gerçek görüntü ağırlıklı; mekanizmada özgün şema |
| Eldeki malzeme | Ekli dosyalar ve gerçekten elindeki kaynaklar | Bir fotoğraf var; klip henüz yok |
| Üretim zamanı | İnsan çalışma süren | En fazla 3 saat; aşarsa daha sade sürüm öner |
| Ek harcama | Bu video için ilave satın alma sınırı | Yeni stok veya eklenti satın alma yok |
| AI sınırı | Planlanacak deneme sayısı veya tercih | En fazla 2 görsel denemesi; AI video 0 |
| Araçlar | Kullanacağın mevcut uygulamalar | Premiere, After Effects, ElevenLabs |
| Çıktı | Sohbet mi, dosya mı | Nihai paket ve varsa düzenlenebilir dosyalar |

“Ek harcama yok”, mevcut Adobe veya seslendirme aboneliğinin ücretsiz olduğu anlamına gelmez. Yeni maliyeti sınırlamak istediğini anlatır. “En fazla 2 deneme” de gerçekleşmiş üretim değil, planlanan sınırdır. Kredi bedeli modele göre değişiyorsa güncel bilgi veya senin verdiğin değer gerekir.

Belirtmediğinde varsayılan yaklaşım Türkçe, genel izleyici, 30–40 saniye, 9:16, kendi çekimi ve sunucu olmadan, yeni satın alma gerektirmeyen plandır. İngilizce hedefliyorsan bunu her yeni projede açıkça yaz.

## 4 Kopyalanabilir kısa brief

Bu mesaj günlük kullanım için yeterlidir. Skill'i seçtikten sonra gönder.

```text
Konu: [TEK KONU VEYA SORU]
Seslendirme dili: [DİL]
Üretim ve edit notlarının dili: Türkçe
Hedef izleyici: Konuya yabancı genel izleyici
Hedef süre: [SÜRE VEYA ARALIK]

Kendi çekimim yok; gerçek görüntüler ve fotoğraflar öncelikli.
Gerektiğinde anlaşılır özgün şema kullan.
Ek harcama: [SINIR]
AI sınırı: [TERCİH VEYA DENEME SAYISI]
Mevcut malzeme ve kaynaklar: [EKLE VEYA HENÜZ YOK YAZ]

Araştırmadan son kontrole kadar akışı kendin tamamla.
Ara aşamalarda rutin onay isteme. En iyi uygulanabilir yaklaşımı seç.
Seçilmiş hook, temiz seslendirme, saniye planı, sahneler, görsel arama,
gereken AI promptları ve edit planından oluşan nihai paketi ver.
Eksikleri ve doğrulanmamış bilgileri açıkça işaretle.
```

## 5 Kopyalanabilir gelişmiş brief

Bu örnek, bütün iş akışını ayrıntılı yönetmek istediğinde kullanılabilir. Alanların tamamı zorunlu değildir. Örnek değerleri kendi projen için değiştir.

```text
PROJE
Konu: Fermuarın sürgüsü iki taraftaki dişleri nasıl birleştiriyor?
Kanal sütunu: Nesnelerin gizli tasarımı ve mekanizmaları.
Amaç: İzleyici video sonunda sürgünün işlevini görsel olarak anlayabilsin.
Tek videoda fermuar tarihini ve bütün fermuar türlerini anlatma.

İZLEYİCİ VE DİL
Genel ve teknik bilgisi olmayan izleyici.
Seslendirme: Doğal İngilizce.
Edit açıklamaları, araştırma özeti ve üretim notları: Türkçe.
Ekran yazıları: İngilizce.

SÜRE VE ANLATIM
Hedef süre 35 saniye; açıklık için gerekiyorsa 30–40 saniye içinde kal.
İlk görüntü ve ilk cümle aynı merakı kursun.
Selamlaşma, logo girişi ve “sonuna kadar izle” kullanma.
Cevabı gösterecek görüntüyü senaryo seçimine dahil et.
Cevabı erken vermek daha iyi çalışıyorsa devamı nasıl sorusuyla ilerlesin.
Gerçek olay, yaygın inanış veya teknik açıklama uydurma.

GÖRSEL VE EDİT
Kendi çekimim ve kamerada görünen sunucum yok.
Gerçek ürün görüntüsü, yakın fotoğraf ve basit özgün şemalar öncelikli.
Premiere ana kurgu, After Effects yalnızca gerekli açıklayıcı sahneler için.
Gösterilemeyen bir mekanizmayı rastgele stok videoyla geçiştirme.
Her sahnede tam olarak ne göreceğimi ve neyi anlayacağımı yaz.
Bulunmayan görüntü için uygulanabilir düşük maliyetli alternatif ver.

ZAMAN VE MALİYET
Üretime ayırabileceğim örnek üst sınır: 3 saat.
Mevcut araçlarıma ek yeni stok, eklenti veya abonelik satın alma yok.
AI video planlama. Gerekliyse en fazla 2 AI görsel denemesi planlayabilirsin.
Kesin mekanik oranlar ve hareketler için doğru özgün şema tercih et.
İş yükü sınırı aşıyorsa minimum uygulanabilir sürümü seç.
Fiyat veya kredi bilgisi bilinmiyorsa tahminini kesin bedel gibi sunma.

ELİMDEKİLER
Kaynaklar: [URL VEYA KAYNAK METİNLERİNİ EKLE]
Görüntüler: [DOSYA ADLARI VE KULLANIM DURUMUNU EKLE]
Henüz bulunmamış malzemeleri mevcut sayma.

ÇALIŞMA BİÇİMİ
Kanal kurallarını ve ilgili rehber bölümlerini oku.
Araştırma, konu daraltma, hook, senaryo, storyboard, malzeme,
edit ve son kontrol aşamalarını kendin sırayla yürüt.
En güçlü uygulanabilir hook'u seç; bir yedeğini tut.
Rutin tercihler için benden onay bekleme.
Ana cevabı değiştiren kritik eksikte en fazla 3 somut soru sor;
bağımsız planlama işlerini yine ilerlet.

TESLİM
Önce nihai durum ve kritik eksikler, ardından seçilen hook ve temiz metin.
Ana metne ek olarak daha kısa seslendirme yedeği ver.
Sahne zamanları ve metin eşleşmeleri kesintisiz olsun.
Her sahne için görüntü, kadraj, ekran yazısı, edit amacı ve alternatif yaz.
Gerçek malzeme arama sorguları ve bulduysan gerçek bağlantıları ekle.
Gereken AI görsel promptlarını İngilizce hazırla.
Video içindeki süre ile benim çalışma süremi ayrı hesapla.
Kaynakları, hak kontrol durumunu ve kontrol sonucunu göster.
Üç dürüst başlık, kısa açıklama ve bir izleyici hipotezi ekle.
Araçların destekliyorsa final Markdown paketi, proje durumu ve
makine kontrolü için JSON özeti oluştur. Dosya oluşturamıyorsan
aynı içeriği sohbette ver; hayalî indirme bağlantısı verme.
Görsel üretimi, ücretli işlem veya yayın başlatma; üretim planı hazırla.
```

Bu briefin amacı modelin bütün yaratıcı kararlarını önceden kilitlemek değildir. Ana vaat, kısıtlar ve teslim biçimini netleştirir; uygun anlatım açısını seçmesine alan bırakır.

## 6 Tek görsel üzerinden test

Bir fotoğraf ekleyerek test yapabilirsin. Fakat fotoğrafın ne işe yarayacağını belirt: Konu kaynağı mı, açılış görseli mi, görsel stil referansı mı? Bunlar farklı görevlerdir.

- **Konu görseli:** Fotoğraftaki nesne veya ayrıntıdan bir açıklama sorusu çıkarılır.
- **Açılış görseli:** Konu bellidir; fotoğraf ilk sahnede kullanılabilecek malzemedir.
- **Stil referansı:** Kompozisyon veya anlatım hissi örnektir; fotoğraftaki her iddia konuya taşınmaz.

Örnek görsel briefi:

```text
Eklediğim görseli bu projenin başlangıç malzemesi olarak kullan.
Görselin görevi: [KONU GÖRSELİ / AÇILIŞ / STİL REFERANSI]

Önce fotoğrafta doğrudan görülen ayrıntıları, emin olmadığın
tanımlamaları ve dış kaynak gerektiren açıklamaları ayır.
Fotoğrafı gerçekten inceleyemiyorsan bunu söyle; bakmış gibi davranma.
Ürün modeli veya hayvan türü kesin değilse tahminini doğrulanmış sayma.

Bu görselden kanalımızın üç alanından birine uygun tek bir merak sorusu seç.
Uygun değilse zorlamadan belirt ve yakın bir alternatif öner.

Seslendirme İngilizce, plan Türkçe, yaklaşık 30–35 saniye olsun.
Kendi çekimim yok. Yeni satın alma yok. AI video istemiyorum.
Gerçek görüntü bulunamazsa fotoğraf hareketi, özgün şema veya uygun
AI görsel için prompt öner. Sentetik görüntüyü gerçek kanıt gibi kullanma.

Fotoğrafın kullanım hakkı: [BANA AİT / İZİNLİ / HENÜZ BİLİNMİYOR]
Hak durumu bilinmiyorsa planı test için hazırlayabilirsin;
fotoğrafı yayın için kullanımı onaylanmış sayma.

Tüm akışı tek seferde tamamlayıp nihai üretim paketini sun.
Bu denemede görsel veya video üretme; yalnızca kurgu ve üretim planı hazırla.
```

Bir fotoğrafta görünmeyen iç mekanizma, ürünün üretim amacı veya hayvanın davranış nedeni doğrudan kanıtlanmış olmaz. Fotoğraf, konuyu seçmeye ve sahne kurmaya yardımcı olur; açıklama için kaynak araştırması devam eder.

“Bir görsel üzerinde test” ile kastın doğrudan o görseli değiştirmekse bunu ayrıca belirtmelisin. Mevcut skill'in ana çıktısı kurgu paketidir; resim düzenleme aracı değildir.

## 7 Üç konu alanı için başlangıç örnekleri

### Nesne

```text
Konu: Fermuar sürgüsünün iki tarafı birleştirmesi.
İngilizce ses, Türkçe plan, 35 saniye.
Gerçek yakın çekim veya doğru özgün şema kullan.
AI video 0, ek satın alma yok. Tam üretim paketini hazırla.
```

### Hayvan

```text
Konu: Narvalın uzun çıkıntısının ne olduğu.
İngilizce ses, Türkçe plan, 30 saniye.
Tek anatomi sorusuna odaklan; bütün işlevlerini anlatma.
Türü doğru gerçek görüntü kullan. Hayalî davranış sahnesi ekleme.
Kaynak ve malzeme durumunu açık tut. Tam paketi hazırla.
```

### Bilim ve ölçek

```text
Konu: Dünya ile Ay arasındaki uzaklığı ölçekli çizince ne görüyoruz?
İngilizce ses, Türkçe plan, 35 saniye.
Merkezler arası mesafe ile yüzeyler arasındaki boşluğu ayır.
Hesap ve birimleri kaynaklandır; şemayı kesin oranlarla planla.
Ölçek için AI görüntüsüne güvenme. Ek satın alma yok. Tam paketi hazırla.
```

Bu örnekler konu briefleridir; açıklamalarının önceden doğrulandığı veya hepsinin gerçek kullanım testini geçtiği anlamına gelmez.

## 8 Sonuçta ne teslim alacaksın

| Bölüm | Kullanacağın yer |
|---|---|
| Durum ve varsayımlar | Hangi eksiklerin kaldığını görme |
| Ana hook ve yedek | Açılışı kurma |
| Temiz seslendirme | Ses kaydı veya seslendirme aracına aktarma |
| Kısa metin yedeği | Süreyi azaltma |
| İddia ve kaynak eşlemesi | Bilgi kontrolü |
| Zaman çizelgesi | Timeline iskeleti |
| Sahne kartları | Kadraj, görüntü, yazı ve edit uygulaması |
| Malzeme listesi | Görüntü edinme ve hak takibi |
| Şema ve gerekli AI promptları | Eksik açıklayıcı sahneleri hazırlama |
| İş planı ve süre aralıkları | Kendi çalışma zamanını yönetme |
| Son kontrol | Düzeltilen ve açık kalan sorunları ayırma |
| Başlık, açıklama ve hipotez | Yayın hazırlığı ve sonraki öğrenme |

Çıktının durumunu doğru oku:

- **PROVISIONAL:** Ana bilgi, kritik görsel veya önemli bir çelişki henüz çözülmemiş. Yararlı taslak var; yayın hazırlığı tamamlanmış değil.
- **PLANNED:** Üretim planı tamamlanmış; malzemeleri edinme, seslendirme ve uygulama işleri kalabilir.
- **EDIT READY:** Gerekli kaynaklar ve malzemeler kontrol edilmiş, hak dayanakları kaydedilmiş ve ses üzerinden zamanlama yeniden yapılmış. Bu etiket bitmiş video veya platform onayı değildir.

İlk çalıştırmada elinde ses ve görseller yoksa PLANNED veya PROVISIONAL almak olağandır. Sürecin doğru eksikleri bildirmesi, yapılmayan işi yapılmış gibi göstermesinden daha kullanışlıdır.

## 9 Revizyon ve gerçek ses süresine uyarlama

### Açılışı değiştirme

```text
Ana soruyu ve doğrulanmış cevabı koru.
Mevcut hook fazla genel. İlk karede [AYRINTI] görünsün.
İlk cümleyi bu görüntüyle doğrudan ilişkilendir.
En iyi yeni hook'u seç; etkilenen senaryo, zamanlama ve sahneleri güncelle.
Değişmeyen bölümleri gereksiz yeniden yazma. Yeni sürüm V2 olsun.
```

### Ses kaydı uzun geldiğinde

```text
Bu paketin gerçek seslendirmesi 42 saniye çıktı; hedefim 35 saniye.
Ses dosyası veya cümle zamanları: [EKLE]
Ana açıklamayı ve doğruluk sınırını koruyarak metni kısalt.
Yeni temiz metni, güncel sahne planını ve değişen malzemeleri ver.
Yeniden seslendirme gerekiyorsa açıkça belirt.
Sadece konuşmayı hızlandırıp süreye sığdırmayı varsayma.
```

### Görüntü bulunamadığında

```text
S03 için önerilen klibi bulamadım. Elimde yalnızca [DOSYA] var.
Aynı açıklamayı koruyarak sahneyi fotoğraf hareketi veya özgün şemayla çöz.
Gerekirse AI görsel promptu ver; yeni video üretimi planlama.
Sahneyi, ilgili ses cümlesini ve toplam süreyi birlikte güncelle.
```

### Yeni sohbete geçerken

```text
Bu projeyi yeni sohbete taşıyacağım.
Son sürümün briefini, seçili hook'unu, temiz metnini, kaynak durumunu,
malzeme ID'lerini, zaman/bütçe sınırlarını ve açık işleri özetle.
Doğrulanmamış bilgileri doğrulanmışa dönüştürme.
Ayrıca hangi dosyaları yeni sohbete eklemem gerektiğini listele.
```

Dosya çıktısı varsa son `production-package.md`, `project-state.json` ve kaynak/malzeme kayıtlarını da taşı. Özet, ayrıntılı storyboard'un tamamının yerine geçmeyebilir.

## 10 Görsel bulunamadığında ve araçlar eksik olduğunda

Görsel araştırması önce gerekli ayrıntıyı tarif eder. Web ve medya araçları varsa adayları araştırır; erişemediği klibi izlemiş saymaz. Arama sorgusu teslim edilmesi, dosyanın edinildiği anlamına gelmez.

Alternatif sırası mevcut malzeme, uygun gerçek görüntü/fotoğraf, özgün şema ve gerekiyorsa AI görsel/video olabilir. Sıranın amacı maliyeti azaltırken açıklamayı korumaktır. Kullanıcının sınırları bu seçimi değiştirir.

AI görsel gerekiyorsa skill prompt hazırlar. Otomatik görsel üretimi için ayrıca açık talimat ve uygun araç gerekir. “Prompt yaz” ile “görseli üret” farklı işlemlerdir. Satın alma veya yayın, hazırlık planının otomatik parçası değildir.

Web erişimi yoksa kaynak metinlerini ekleyebilirsin. Yalnızca URL vermek modelin o sayfayı incelediğini göstermez. Dosya yazma veya Python yoksa paket sohbet içinde sunulur; yapısal kontrolün çalıştırılamadığı belirtilir.

## 11 İlk testleri değerlendirme

İlk üç denemeyi farklı alanlardan seç. Sonra en uygulanabilir paketin en az bir bölümünü gerçekten editle. Değerlendirme için şu sorular yeterli bir başlangıçtır:

1. Ana soruyu ve cevabı birer cümlede söyleyebiliyor muyum?
2. İlk görüntüyü eldeki araç ve malzemeyle kurabiliyor muyum?
3. Temiz metin doğal okunuyor ve süresine sığıyor mu?
4. Her sahnede ne gösterileceği açık mı?
5. Gereken dosya ile sadece arama hedefi ayrılmış mı?
6. Eksik görüntü için verilen alternatif gerçekten yapılabilir mi?
7. Kaynak, tür/model, oran ve kullanım hakkı durumu anlaşılır mı?
8. Tahmini iş yükü benim üretim hızımla uyumlu mu?
9. Nihai metin ve uygulanacak sahneleri çıktıda kolay bulabiliyor muyum?
10. AI yapılmayan bir işi yapılmış gibi göstermiş mi?

Test notunu şu şekilde tut:

```text
Paket sürümü veya Git commit'i:
Konu ve tarih:
Model ve mevcut araçlar:
Kullandığım brief:
İşe yarayan kısım:
Uygulanamayan sahne veya sorun:
Gerçek araştırma / malzeme / edit sürem:
İstediğim düzeltme:
```

Otomatik kontrolleri terminalde çalıştırmak istersen repo kökünde:

```bash
python3 tests/test_validator.py
```

Skill'in oluşturduğu makine özeti için:

```bash
python3 skills/create-curiosity-shorts/scripts/validate_package.py production-package.json
```

Bu kontrol, skill'in kendi şemasına uygun JSON bekler. Yalnızca süre ve yapısal tutarlılık gibi alanları denetler; anlatımın iyi olduğunu veya bilginin doğru olduğunu kanıtlamaz. Daha kapsamlı senaryolar `tests/scenarios.md` içinde.

## 12 Sık karşılaşılan sorunlar

| Sorun | Gönderilecek düzeltme |
|---|---|
| Yalnızca senaryo verdi | “Çıktı sözleşmesindeki eksik sahne, malzeme, edit ve audit bölümlerini tamamla.” |
| Her aşamada onay bekliyor | “Rutin tercihleri kendin seçip akışı tamamla; yalnızca kritik eksikleri sor.” |
| Uzun ve dağınık çıktı | “Seçilen hook ve temiz metni başa al; elenen fikirleri çıkar, uygulanacak sahneleri koru.” |
| Sahne çok genel | “S03'teki nesneyi, hareketi, kadrajı, ekran yazısını ve malzemeyi kesinleştir.” |
| Konu pahalı görünüyor | “Ana cevabı koruyan minimum uygulanabilir sürümü kur; ücretli ve zor sahneleri sadeleştir.” |
| Görsel mevcut sanılmış | “Bu malzeme edinilmedi. Durumunu ARANACAK yap, bağlantı ve hak durumunu yeniden değerlendir.” |
| Kaynak okunmadan doğrulanmış denmiş | “İddiayı doğrulanmamış olarak işaretle. Kaynağın ilgili bölümünü incele veya metni iste.” |
| Ses İngilizce istenmesine rağmen Türkçe | “Seslendirme ve ekran yazısı İngilizce; üretim notları Türkçe olacak şekilde güncelle.” |
| Süreler tutmuyor | “Sahne sürelerini yeniden topla, boşluk ve çakışmaları düzelt; ses tahminini tekrar hesapla.” |

Skill'i geliştirmek için yalnızca “olmadı” demek yerine sahne ID'si ve somut sorun ver. Birden çok projede tekrarlanan hata, talimatlara kalıcı düzeltme eklemek için iyi bir adaydır.

## 13 Dosyaların görevleri ve resmî kaynaklar

| Dosya veya klasör | Görevi |
|---|---|
| `README.md` | Repo özeti ve kısa kurulum |
| `START.md` | Kurulum olmadan, erişilebilir repodan akışı başlatma mesajı |
| `skills/create-curiosity-shorts/SKILL.md` | Tek brief ile süreci yöneten ana talimat |
| `references/workflow.md` | Araştırmadan teslime ayrıntılı aşamalar |
| `references/channel-rules.md` | Niş, görsel dil ve üretim tercihleri |
| `references/quality-rules.md` | Durum etiketleri, doğruluk ve tamamlanma kontrolleri |
| `references/capabilities.md` | Araçlar eksikken nasıl davranılacağı |
| `references/complete-guide.md` | 29 sayfalık rehberin metin ve tablolarının tamamı |
| `assets/production-handbook-v2.docx` | Orijinal Word rehberi |
| `assets/production-package.md` | Nihai teslim bölümleri |
| `assets/project-state.json` | Aşamaların ve kararların kaydı için başlangıç şablonu |
| `assets/production.schema.json` | Makine özetinin şeması |
| `scripts/validate_package.py` | Zaman/yapı kontrolü |
| `tests/` | Kontrol betiği testleri ve gerçek kullanım senaryoları |
| `VALIDATION.md` | Gerçekte yapılan testlerin kapsamı ve sınırları |
| `coverage.json` | Rehber aktarımının kapsam kaydı |

`references/`, `assets/` ve `scripts/` yolları tabloda skill klasörüne göredir. Dosyaları dağıtırken birbirinden koparma.

Kurulum ve ürün davranışı için kontrol edilen resmî kaynaklar:

- [ChatGPT başlangıç ve hesapla giriş](https://learn.chatgpt.com/docs/quickstart)
- [Skill oluşturma, çağırma ve yerel kurulum](https://learn.chatgpt.com/docs/build-skills)
- [Plugin paketleme](https://developers.openai.com/plugins/build/plugins)

Kontrol tarihi 15 Ekim 2026. Paket bir iş akışı sağlar; hesabındaki menülerin, araç erişimlerinin veya platform dağıtımının yerini almaz. Kurulumda farklı bir ekran görürsen önce kullanılan uygulama, sürüm ve çalışma modunu netleştir.
