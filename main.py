from Muzisyen import Muzisyen
from Gitar import Gitar
from Bateri import Bateri

gitar = Gitar()
gitar.Marka = "Yamaha"
gitar.Aciklama = "Pahalı"
sound = gitar.Cal()

muzisyen = Muzisyen()
muzisyen.Adi = "Simge "
muzisyen.Soyadi = "Karademir"
muzisyen.Enstruman = gitar

result = """
Adı      : {}
Soyadı   : {}
Enstruman: {}
Marka    : {}
Açıklama : {}
""".format(muzisyen.Adi,muzisyen.Soyadi,sound,muzisyen.Enstruman.Marka,muzisyen.Enstruman.Aciklama)
print(result)