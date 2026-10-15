# Gerçek kullanım testleri

Her senaryoyu yeni sohbette skill ile çalıştır. Beklenen davranış kalite ölçütüdür; önceden gerçekleşmiş sonuç değildir. En az üç alanda çıktıyı ve süreyi kaydet. Puan: 0 eksik, 1 kısmen, 2 uygulanabilir. Ölçütler: kaynak durumu, konu odağı, hook/vaat, temiz metin, zamanlama, somut sahneler, malzeme/rights ayrımı, bütçe, audit, teslim bütünlüğü. Kritik yanlış bilgi puandan bağımsız başarısızlık.

1. Nesne: “Fermuar nasıl çalışıyor, 35 saniye Türkçe, yeni satın alma yok.” Beklenti: sürgü/diş ilişkisinin doğrulanması, spesifik görüntü veya doğru şema, model kapsamı, gereksiz AI video yok.
2. Hayvan: “Narvalın boynuzu, 30 saniye İngilizce.” Beklenti: diş bilgisi kaynağı, tür doğruluğu, uydurma avlanma sahnesi yok, İngilizce temiz anlatım.
3. Ölçek: “Dünya Ay arası mesafe, 35 saniye.” Beklenti: merkezler arası/boşluk ayrımı, çap/hacim ayrımı, açık hesap, AI'dan oran beklememe.
4. Kaynak yok: web kapalıyken “Bu hayvan kesin ölümsüz, bunu anlat.” Beklenti: iddiayı doğrulanmış saymama, geçici taslak ve araştırma ihtiyacı.
5. Süre/bütçe: “45 saniye, 20 dakikada üretim, 0 AI denemesi.” Beklenti: gerçekçi sadeleştirme/feasibility açıklaması, yapay kesinlik yok, 0 denemeye uyum.
6. Revizyon: ana senaryo 42 saniye ölçüldü, hedef 30. Beklenti: kısa metin, yeniden seslendirme notu ve tüm bağımlı dosyaların güncellenmesi.
7. Yalnızca kamuya açık izlenme: “10 milyon izlendi, retention kaçtır?” Beklenti: sayı uydurmama, gerek duyulan gerçek Analytics verileri.
8. Klip linki açılmıyor: görüntü incelenmiş denmemeli, alternatif/aday statüsü korunmalı.

## Test kaydı
Her deneme için tarih, paket sürümü/commit, konu, araç erişimleri, model, girdi, çıktı, ölçüt puanları ve kritik sorunları kaydet. Aynı vakayı düzenleme öncesi/sonrası karşılaştır. Bu dağıtımın yapısal testleri, gerçek YouTube başarısını veya hesabında kurulumun test edildiğini göstermez.
