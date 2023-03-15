
class Matematik:
    def __init__(self, sayi1, sayi2): 
        print("Matematik başlatildi (referans'i oluştu)")
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2


matematik = Matematik(14, 7)

sonuc = matematik.topla()
print("Toplama Sonucu: "+str(sonuc))

sonuc = matematik.cikar()
print("Çikartma Sonucu: "+str(sonuc))

sonuc = matematik.carp()
print("Çarpma Sonucu: "+str(sonuc))

sonuc = matematik.bol()
print("Bölme Sonucu: "+str(sonuc))

#inheritance
class Istatistic(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
    
    def varyansHesapla(self):
        return self.sayi1 * self.sayi2
    
istatistic = Istatistic(5, 8) 
istatistic.topla()
istatistic.cikar()
istatistic.carp()
istatistic.bol()
istatistic.varyansHesapla()
