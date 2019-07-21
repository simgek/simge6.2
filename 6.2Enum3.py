from enum import Enum, unique

@unique
class Icecek (Enum):
    Vanilya  = 7
    Çikolata = 4
    Vişne    = 3
    Muzlu    = 1
    #Kiraz    = 7 sınıf içerisinde aynı değere sahip eleman bulunamaz

for x in Icecek:
    print(x)

for ad, uye in Icecek.__members__.items():
    print(str(ad) + " " + str(uye))
    print(str(ad), str(uye))
    print(ad , uye)