from enum import Enum

class Renkenum(Enum):
    Kırmızı = 1
    Sarı = 2
    Mavi = "Blue"

print(repr(Renkenum.Mavi))

class Intenum(int, Enum):
    # birinci parametrede verilen veri tipi ne ise içerde tanımladığınız value dğeride o tipte olmak zorundadır
    Kırmzı = 1
    Sarı = 2
    #Mavi = "mavi"

print(Intenum.Sarı.value)

class Floatenum(float, Enum):
    Kırmızı = 1
    sarı = 0.9

print(Floatenum.sarı.value)
