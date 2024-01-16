class Zviera:
    def hlas(self):
        raise NotImplementedError("Podtrieda musi implementovat tuto podtriedu")

class Pes(Zviera):
    def hlas(self):
        return "How"
    def koncatiny(self):
        return 5
class Kohut(Zviera):
    def hlas(self):
        return "Kikirik"
    def koncatiny(self):
        return 2
class Macka(Zviera):

    def koncatiny(self):
        return 5
def vydaj_zvuk(Zviera):
    return zviera.hlas()

def koncatiny(Zviera):
    return zviera.koncatiny()


pes = Pes()
macka = Macka()
kohut = Kohut()

for zviera in [pes, macka, kohut]:
    print(vydaj_zvuk(Zviera))

for zviera in [pes, macka, kohut]:
    print(koncatiny(Zviera))

for zviera in [pes, macka, kohut]:
    print(zviera.hlas())
