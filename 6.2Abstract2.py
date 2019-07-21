from abc import ABCMeta, abstractmethod


class BasePhone(metaclass = ABCMeta):
    __metaclass__ = ABCMeta

    def _init__(self, marka, model, fiyat):
        self.Marka = marka
        self.Model = model
        self.Fiyat = fiyat

    @abstractmethod
    def Sound(self):
        return "çan sesi"


class Samsung(BasePhone):
    def __init__(self, marka, model, fiyat, tedarikci):
        super(Samsung, self).__init__(marka,model,fiyat)
        self.Tedarikci = tedarikci

    def Sound(self):
        return "samsung default mobile phone sound";

class Apple(BasePhone):
    def __init__(self, marka, model, fiyat, garanti):
        super(Apple, self).__init__(marka,model,fiyat)
        self.Garanti = garanti

    def Sound(self):
        return "Apple default mobile phone sound";

apple = Apple("Apple", "8sPlus", 10000, "tr")
print("""
Marka        : {}
Model        : {}
Fiyat        : {}
Garanti      : {}
Telefon sesi : {}
""".format(apple.Marka, apple.Model, apple.Fiyat, apple.Garanti, apple.Sound()))

samsung = Samsung("Samsung", "S10Plus", 10000, "KVK")
print("""
Marka        : {}
Model        : {}
Fiyat        : {}
Tedarikci    : {}
Telefon sesi : {}
""".format(samsung.Marka, samsung.Model, samsung.Fiyat, samsung.Tedarikci, samsung.Sound()))