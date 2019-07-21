class Personel:

    def __init__(self, isim, soyisim):
        self.Firstname = isim
        self.Lastname  = soyisim

    @property
    def email(self):
        return "{}.{}".format(str(self.Firstname).lower(),str(self.Lastname).loweer())

    @property
    def isim_soyisim(self):
        return "{} {}".format(self.Firstname,self.Lastname)

    @isim_soyisim.setter
    def isim_soyisim(self,parametre):
        ad,soyad = parametre.split(' ')
        self.Firstname = ad
        self.Lastname  = soyad

    @isim_soyisim.deleter
    def isim_soyisim(self):
        print("kişi silindi")
        self.Firstname = None
        self.Lastname  = None



    per1 = Personel("simge","karademir")
    print(per1.Firstname)
    print(per1.Lastname)
    print(per1.email)

    per1 = Personel("okan", "muzikacı")
    print(per1.Firstname)
    print(per1.Lastname)
    print(per1.email)


