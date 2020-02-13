
class Prikaz:
    def __init__(self, stranica, rang):
        self._stranica = stranica
        self._rang = rang

    def get_stranica(self):
        return self._stranica

    def get_rang(self):
        return self._rang

    def set_rang(self, rang):
        self._rang = rang


def prvo_rangiranje(stranica, trie, br_ulaznih_cvorova, lista_reci = []):
    rang = 200
    """
    for rec in lista_reci:
    rang += trie.search(rec)[1]
    """
    rang = rang * 0.5  # rangiramo za svako pojavljivanje reci - svako pojvaljivanje += 0.5
    rang += br_ulaznih_cvorova  # za svaki ulazni cvor += 1

    return Prikaz(stranica, rang)

def drugo_rangiranje(pocetni_rang, mapa_prikaza, lista_ulaznih_cvorova, mnozilac,graph):
    zbir = 0
    for cvor in lista_ulaznih_cvorova:
        if mnozilac < 0.05:
            zbir += mapa_prikaza[cvor]
        else:
            return pocetni_rang + drugo_rangiranje(mapa_prikaza[cvor], mapa_prikaza, graph.get_incoming(cvor), mnozilac/3, graph)

    return zbir*mnozilac
