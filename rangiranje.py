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


def prvo_rangiranje(stranica, trie, niz_reci):
    rang = 0

    for rec in niz_reci:
        rang += trie.search(rec)[1]

    rang = float(rang) * 0.5  # rangiramo za svako pojavljivanje reci - svako pojvaljivanje += 0.5

    return Prikaz(stranica, rang)


def drugo_rangiranje(pocetni_rang, mapa_prikaza, lista_ulaznih_cvorova, mnozilac, graph):
    zbir = 0
    for cvor in lista_ulaznih_cvorova:
        if mapa_prikaza.keys().__contains__(cvor):
            if mnozilac < 0.01:
                zbir += mapa_prikaza[cvor]
            else:
                return pocetni_rang + drugo_rangiranje(mapa_prikaza[cvor], mapa_prikaza, graph.get_incoming(cvor),
                                                           mnozilac / 3, graph)
        else:
            if mnozilac < 0.01:
                pass
            else:
                return pocetni_rang + drugo_rangiranje(0, mapa_prikaza, graph.get_incoming(cvor),
                                                           mnozilac / 3, graph)

    return zbir * mnozilac
