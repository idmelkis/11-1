class Restorans:
    _darbinieki: 'list[Darbinieks]'
    _virtuve: 'Virtuve'
    def __init__(self) -> None:
        self._darbinieki = []
    def AprekinatDarbiniekuAlgas(self) -> float:
        algas = 0.0
        for darbinieks in self._darbinieki:
            algas += darbinieks.IzvaditAlgu()
        return algas
    def PirktEdienus(self, klients: 'Klients', receptes: 'list[Recepte]') -> 'list[Ediens]':
        viesmilis = None
        for darbinieks in self._darbinieki:
            if type(darbinieks) == Viesmilis:
                viesmilis = darbinieks
                break
        # Šeit vajadzētu ēdiena sagataves loģiku
class Darbinieks:
    _alga: float = 100.0
    def IzvaditAlgu(self):
        return self._alga
class Pavars(Darbinieks):
    _alga = 200.0
class Viesmilis(Darbinieks):
    _dzeramnauda: float
    def __init__(self) -> None:
        self._alga = 150.0
        self._dzeramnauda = 0.0
    def IzvaditAlgu(self):
        return super().IzvaditAlgu() + self._dzeramnauda
class Recepte:
    _instrukcijas: 'list[str]'
    _sastavdalas: 'list[Sastavdala]'
    def __init__(self, instrukcijas, sastavdalas):
        self._instrukcijas = instrukcijas
        self._sastavdalas = sastavdalas
    def AprekinaIzmaksas(self) -> float:
        cena = 0.0
        for sastavdala in self._sastavdalas:
            cena += sastavdala.IzvaditIzmaksas()
        return cena
class Ediens:
    _sastavdalas: 'list[Sastavdala]'
    def __init__(self, sastavdalas):
        self._sastavdalas = sastavdalas
    def AprekinaIzmaksas(self) -> float:
        cena = 0.0
        for sastavdala in self._sastavdalas:
            cena += sastavdala.IzvaditIzmaksas()
        return cena
class Sastavdala:
    _izmaksas: float
    _daudzums: float
    def __init__(self, izmaksas: float, daudzums: float) -> None:
        self._izmaksas = izmaksas
        self._daudzums = daudzums
    def IzvaditIzmaksas(self) -> float:
        return self._izmaksas*self._daudzums
class Virtuve:
    _sastavdalas: 'list[Sastavdala]'
class Klients:
    _nauda: float

kartupeli = Sastavdala(0.1, 2.0)
print(kartupeli.IzvaditIzmaksas())

virtuve = Virtuve()
Janis = Darbinieks()
Reinis = Pavars()
Anna = Viesmilis()
restorans = Restorans()
restorans._darbinieki.append(Janis)
restorans._darbinieki.append(Reinis)
restorans._darbinieki.append(Anna)
print(restorans.AprekinatDarbiniekuAlgas())