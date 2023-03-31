# Python-Selenium-Bootcamp
Kodlama.io platformunda bulunan "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium" adlı eğitimin notları ve ödevleri.

Eğitmen: Halit Enes Kalaycı

Dekoratörler diğer fonksiyonların işlevselliğini değiştiren fonksiyonlardır. Kodu kısaltırlar ve daha anlaşılır hale getirirler.Bir dekoratör aslında fonksiyon çağıran bir fonksiyondan başka bir şey değildir. Başında @ işareti kulanılarak koda dahil edilebilir. Buna pie syntax denir. Kendisinden önce, @ işareti ile geldiği fonksiyonu çalıştırmadan önce kendi içinde wrapped edilmiş işleri yapar ve sonra kendisinden sonra gelen fonksiyonu çağırarak onun görevini yerine getirmesini sağlar.

Pytest, bir Python test çerçevesidir ve test yazarken kullanabileceğiniz bir dizi dekoratöre sahiptir. Bu dekoratörler, testleri yürütürken nasıl davranacaklarını belirlemek için kullanılır. Bazı yaygın pytest dekoratörleri şunlardır:

    @pytest.fixture: Bu dekoratör, testlerinizde kullanmak için bir "fixture" oluşturmanızı sağlar. Bir "fixture", örneğin bir veritabanı bağlantısı veya bir örnek gibi, testlerinize bir kaynak sağlar.

    @pytest.mark.parametrize: Bu dekoratör, aynı testin farklı parametrelerle birden çok kez çalıştırılmasını sağlar. Bu özellikle bir dizi girişle çalışan testler için yararlıdır.

    @pytest.mark.skip: Bu dekoratör, bir testin belirtilen nedenlerle atlanmasını sağlar. Örneğin, bir test sadece belirli bir platformda çalışıyorsa, diğer platformlarda bu testi atlayabilirsiniz.

    @pytest.mark.xfail: Bu dekoratör, bir testin başarısız olmasını beklediğinizi belirtir. Bu, hataların düzeltilmesi gereken testler üzerinde çalışırken yararlıdır.

    @pytest.mark.timeout: Bu dekoratör, bir testin belirli bir sürede tamamlanmasını sağlar. Eğer test belirli bir sürede tamamlanamazsa, test hata verir ve başarısız olur.


