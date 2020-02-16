import globalVar


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


def prvo_rangiranje(niz_reci):
    mapa_prikaza = {}
    for stranica in globalVar.RESULT_SET:
        mapa_prikaza[stranica] = 0  # inicijalno stavljamo da je rang 0

    # prolazimo kroz reci u kriterijumu pretrage
    for rec in niz_reci:
        bool, skup = globalVar.GLOBAL_TRIE.search(rec.lower())  # dobijamo indikator uspesnosti trazenja i set stranica
        if bool == "True":  # ako je uspesno trazenje nastavljamo
            o = skup.getStr()   # skup (recnik) stranica
            for stranica in o:
                if stranica in mapa_prikaza.keys(): # za svaku stranicu iz seta stranica sabiramo broj ponavljanja reci
                    mapa_prikaza[stranica] += o[stranica]

    for stranica in globalVar.RESULT_SET:
        mapa_prikaza[stranica] = mapa_prikaza[stranica] * 0.5 # 1 povaljanje +0.5 rang

    return mapa_prikaza # vracanje recnika, kljuc - putanja stranice, vrednost - trenutni rang


def drugo_rangiranje(mapa_prikaza, lista_ulaznih_cvorova, mnozilac, graph):
    zbir = 0
    i = 0
    # prolazimo kroz sve ulazne grane cvora
    for cvor in lista_ulaznih_cvorova:
        i += 1  # koristimo za proveru kraja
        if mapa_prikaza.keys().__contains__(cvor):
            if mnozilac < globalVar.n:
                zbir += mapa_prikaza[cvor]  # bazni slucaj, odnosno kada dodjemo do poslednjeg reda cvora koji utice
                                            # na rang
            else:
                zbir += drugo_rangiranje(mapa_prikaza, graph.get_incoming(cvor), mnozilac / 3, graph)
                # rekurzivno pozivamo funkciju sa smanjenjem mnozioca (prelazimo na sledeci nivo)
                globalVar.zbir_rangiranje = globalVar.zbir_rangiranje + mapa_prikaza[cvor] * mnozilac
                if i == len(lista_ulaznih_cvorova):
                    globalVar.zbir_rangiranje += zbir
                    zbir = 0
                    globalVar.n *= 3
        else:
            if mnozilac < globalVar.n:
                pass
            else:
                zbir += drugo_rangiranje(mapa_prikaza, graph.get_incoming(cvor), mnozilac / 3, graph)
                if i == len(lista_ulaznih_cvorova):
                    globalVar.zbir_rangiranje += zbir
                    zbir = 0
                    globalVar.n *= 3

    return zbir * mnozilac
