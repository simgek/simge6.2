from enum import Enum

class Durum(Enum):
    Mutlu = 1
    Uzgun = 3

    def describe(self):
        return self.name, self.value

    def __str__(self):
        return "Şuanki ruh halim dıgıdık dıgıdıgık gidiyor ama {} ".format(self.name)

    @classmethod
    def favori_durumum(cls):
        return cls.Uzgun


print(Durum.favori_durumum())
print(Durum.Uzgun.describe())
print(Durum.Mutlu)