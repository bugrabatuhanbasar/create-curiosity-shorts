# Curiosity Shorts Kit

Tek konu mesajından kaynak, seçilmiş hook, seslendirme, zaman çizelgesi, storyboard, görsel arama, gerektiğinde AI promptu, edit ve kontrol paketi üretir. Bitmiş video oluşturmaz. Aşamaları kullanıcıdan tek tek prompt istemeden yürütür.

## Ayrıntılı kullanım kılavuzu

[Kurulum, gelişmiş brief ve görselle test örnekleri](docs/KULLANIM_KILAVUZU.md)

İlk kullanım için bu kılavuzu aç. Kısa ve ayrıntılı kopyalanabilir briefler, revizyon mesajları ve sorun giderme adımları içerir.

## Mac ve hesap
Resmî ChatGPT masaüstü uygulamasını kurup mevcut ChatGPT hesabınla giriş yap. Özellik ve model erişimi hesap/çalışma alanı/sürümüne bağlıdır. Normal sohbete GitHub linki vermek kalıcı kurulum değildir.

## Yerel Codex kurulumu
1. ZIP'i aç. Bu klasörün içeriğini kendi GitHub reponun köküne push et.
2. Masaüstü uygulamasında Codex tarafında Skill Installer'ı seç. CLI/IDE kullanıyorsan `$skill-installer` yaz.
3. Şu talimatı ver: `GitHub depomdaki skills/create-curiosity-shorts klasörünü skill olarak kur: https://github.com/KULLANICI/REPO`. Kullanıcı ve repo alanını gerçek adresinle değiştir. Özel repo erişim isteyebilir.
4. Skill seçicide göründüğünü kontrol et. Görünmüyorsa uygulamayı/Codex'i yeniden başlat.
5. ChatGPT'de @ seçicisinden skill'i seç; Codex CLI/IDE'de `$create-curiosity-shorts` ile çağır. Yerel kurulum web ortamına otomatik kurulum değildir.

## Plugin paketi
Kök plugin.json portable kimliği, .codex-plugin/plugin.json uyumluluk tanımını sağlar; tek gerçek skill skills/ altında bulunur. Bu paket hazırlanmıştır ama OpenAI plugin dizinine gönderilmiş, onaylanmış veya hesabında plugin olarak kurulmuş değildir. Webde kullanılacak plugin için resmî paketleme/kurulum yolunu ve hesap erişimini izle; GitHub'da dosya bulunması tek başına yeterli değildir.

## Kurulum olmadan deneme
START.md içindeki mesajla, depoyu okuyabilen bir sohbette dene. Bütün gerekli referansları okuyamıyorsa ZIP'i ekle. Bu kullanım sadece o sohbetin talimatıdır; skill kurulumu değildir.

## Kullanım
`$create-curiosity-shorts Konu: narvalın uzun dişi. Dil: İngilizce. Süre: 35 saniye. Kendi çekimim yok. Yeni satın alma yok. AI video zorunlu değil. Nihai üretim paketini hazırla.`

## İçerik ve doğrulama
references/complete-guide.md, 29 sayfalık rehberin tüm paragraflarını ve tablo hücrelerini özgün sırada içerir. Orijinal Word belgesi assets/ içinde bulunur. Kaynak/medya/hesap erişimini skill kendiliğinden sağlamaz. Kaynak incelemesi yapılmadığında geçici taslak verir. Araştırma ve üretim tahminleri gerçek izleyici testi değildir.

`python3 tests/test_validator.py` yapısal kontrol betiğinin testlerini çalıştırır. `python3 skills/create-curiosity-shorts/scripts/validate_package.py DOSYA.json` çıktı zamanlamasını ve yapısını kontrol eder. İnternet veya API anahtarı gerekmez. Editoryal kalite ve doğruluk için tests/scenarios.md kullanılır.

## Resmî kaynaklar
Kontrol tarihi: 15 Ekim 2026.
- https://learn.chatgpt.com/docs/quickstart
- https://learn.chatgpt.com/docs/build-skills
- https://developers.openai.com/plugins/build/plugins

Arayüz/dağıtım değişebilir; Skill Installer veya Codex seçeneği hesabında görünmüyorsa mevcut sürüm ve erişimi doğrula. Bu ZIP'in hazırlanması masaüstü hesabında kurulum testi yapıldığı anlamına gelmez.
