class Transportlidzeklis:
    krasa: str
    ritenuSkaits: int
class Automasina(Transportlidzeklis):
    dzinejaTips: str
    def braukt(self):
        return "OK"
class Ritenis(Transportlidzeklis):
    bremzuTips: str

class Zigulis(Automasina):
    def braukt(self):
        #return super().braukt()
        return "Zigulis: OK"
class WVGolf(Automasina):
    def braukt(self):
        return "Golfs: OK"

class Autostavvieta:
    automasinas = []
    #ritenis: Ritenis
    def IzvaditSkaitu(self):
        return len(self.automasinas)

zigulis = Zigulis()
print(zigulis.braukt())
golfs = WVGolf()
print(golfs.braukt())
'''
class nosaukums:
    mainigais: str

    def __init__(self, param):
        self.mainigais = param
    def funkcija(self, param1):
        return param1
    def izvadamMainigo(self):
        print(self.mainigais)
class apaksklase(nosaukums):
    mainigais2: str
    def __init__(self, param):
        print(param)
    def funkcija(self, param1):
        self.mainigais
        return super().funkcija(param1)

objekt3 = apaksklase("apaksklase")

objekts = nosaukums("objekts1")
objekts.izvadamMainigo()
objekts2 = nosaukums("objekts2")
objekts2.izvadamMainigo()

#print(objekts.funkcija(0))
'''