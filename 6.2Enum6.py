#flag kullanımı oluşturduğunuz enum değerlerini benzersiz ve birden fazla enum değerininim bir enum değerine karşılık
# gelmemesi için kullanıır


from enum import Flag, auto, Enum

class Renkler(Flag):
    kırmızı = auto() # enum = 1  flag = 1
    sarı    = auto() # enum = 2  flag = 2
    mavi    = auto() # enum = 3  flag = 4
    turucu  = auto() # enum = 4  flag = 8
    yeşil   = auto() # enum = 5  flag = 16
    pembe   = auto() # enum = 6  flag = 32
    beyaz   = kırmızı | mavi | sarı


#print(repr(Renkler.kırmızı and Renkler.mavi))
liste = list(Renkler)
print(liste)
print(Renkler.kırmızı.value + Renkler.mavi.value + Renkler.sarı.value)
print(repr(Renkler.beyaz))