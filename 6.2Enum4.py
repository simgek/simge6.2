from enum import Enum, unique, auto

@unique
class Icecek(Enum):
    Vanilya  = auto()
    Çikolata = auto()
    Vişne    = auto()
    Muzlu    = auto()
    Çilek    = 35
    kahveli  = auto()

liste = list(Icecek)
print(liste)

