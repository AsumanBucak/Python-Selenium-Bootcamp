# 1-Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

# int, integer: Tam sayılar için kullanılır. 
# int = 7

# float: Ondalıklı sayılar için kullanılır. 
# float = 7.7

# string: Bir veya daha fazla karakter içerir. 
# string = "selenium"

# bool, boolean: Matıksal ifadelerde kullanılır. True ya da False. 
# bool = True

# list: Dizi halindeki veriler için kullanılır. Değiştirilebilir.
# list = [14,48,24,"admin","a"] 

# tuple: Aynı tip verileri bir arada tutmak için kullanılır. Değiştirilemez
# tuple = (1,2,3,4,5,6)

# range : Aralık belirtmek için kullanılır.
# range = range(1,7)

# set: Benzersiz elemanlardan oluşan bir koleksiyondur. Elemanları sıralı değildir ve her eleman sadece bir kez görünür.
# kume = set([1, 2, 3])
# kume.add(3)
# print(kume)

# ----------------------------------------------------------------------------------------------------------------------
# 2-Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# integer : Kurs tamamlama yüzdesi, ödeme kart numarası
# string : yazı ve karakter içeren yerler. Örneğin 'Kurslarım' yazısı.

list_kurslar = ['Yazılım Geliştirici Yetiştirme Kampı',
                "Java",
                "Python & Selenium"]
set_kurslar = set(list_kurslar)
set_kurslar.add("Java")
sozluk_gunler = {"Gun1":"Tanışma",
                 "Gun2":"Python Temelleri"}

# 3-Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
mail = "asuman@gmail.com"
sifre1 = "asuman1234"

mail = input("Lütfen mail adresinizi giriniz: ")
sifre1 = input("Lütfen şifrenizi giriniz: ")

if mail == ("asuman@gmail.com") and sifre1 == ("asuman1234"):
    print("Giriş yapıldı.")
else:
    print("Mail veya şifre yanlış.")