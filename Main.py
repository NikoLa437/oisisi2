from globalVar import *
from mergeSort import mergeSort


def ucitajPodatke(putanja):
    start = time.time()
    parser = Parser()
    for root, dirs, files in os.walk(putanja):
        for file in files:
            if file.endswith('.html'):
                links, words = parser.parse(os.path.join(root, file))
                t = Trie()
                GRAPH.add_from_html(os.path.join(root, file), links)
                for word in words:
                    t.add_word(word.lower())
                    MAPA_TRIE[os.path.join(root, file)] = t
    end = time.time()
    print(end - start)


def obicnaPretraga(kriterijum):
    global RESULT_SET
    RESULT_SET = Skup()
    RESULT_SKUP= []
    for uslov in kriterijum:
        skup = Skup()
        for key in MAPA_TRIE:
            bool, ponavaljanja = MAPA_TRIE[key].search(uslov.lower())
            if bool == "True":
                skup.add(key) # dodaje u skup sve html dokumente koji sadrze datu rec
        RESULT_SKUP.append(skup) # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
    for file in RESULT_SKUP:  # prolazimo kroz skup skupova html dokumenata koji ispunjavaju uslov i radimo logicko | za obicnu pretragu
        RESULT_SET = RESULT_SET | file

def slozenijaPretraga(kriterijum, operacija):
    print("Test: ", operacija)


def rangirajSkup(niz_reci):
    mapa_prikaza = {}
    retVal = []

    # rangiranje na osnovu broja reci u stranicama
    for stranica in RESULT_SET:
        prikaz = rangiranje.prvo_rangiranje(stranica, MAPA_TRIE[stranica], niz_reci)
        mapa_prikaza[prikaz.get_stranica()] = prikaz.get_rang()

    nova_mapa = copy.deepcopy(mapa_prikaza)

    """for el in nova_mapa:
        print(round(nova_mapa[el],2), el)"""

    # rangiranje na osnovu broja reci linkovanim stranicama
    for el in mapa_prikaza:
        mapa_prikaza[el] = rangiranje.drugo_rangiranje(nova_mapa[el], nova_mapa, GRAPH.get_incoming(el), 0.3, GRAPH)

    # rangiranje na osnovu broja linkova
    for el in mapa_prikaza:
        mapa_prikaza[el] = mapa_prikaza[el] + GRAPH.get_incoming(el).__len__()

    for el in mapa_prikaza:
        retVal.append(rangiranje.Prikaz(el, mapa_prikaza[el]))

    mergeSort(retVal)
    return retVal

def paginacijaRezultata(lista_prikaz):
    N = 10
    pocetak = 0
    kraj = 0
    if N > len(lista_prikaz):
        kraj = len(lista_prikaz)
    else:
        kraj = N
    while(True):
        ispisiRezultate(lista_prikaz, pocetak, kraj)
        print("\n")
        print("Izaberite opciju:")
        print("1 - Za prikaz sledecih " + str(N) + " stranica")
        print("2 - Za prikaz prethodnih " + str(N) + " stranica")
        print("3 - Za promenu broja prikazanih stranica")
        print("X - Za izlazak iz pretrage")
        izbor = input("Unesite opciju")

        if izbor == "X" or izbor == "x":
            break
        if izbor == "1":
            pocetak += N
            if kraj + N > len(lista_prikaz):
                kraj = len(lista_prikaz)
            else:
                kraj += N
        if izbor == "2":
            if pocetak - N < 0:
                pocetak = 0
                kraj = N
            else:
                kraj = pocetak
                pocetak -= N

        if izbor == "3":
            n = input("Unesite trazeni broj:")
            N = int(n)
            kraj = pocetak + N

def ispisiRezultate(lista_prikaz, pocetak, kraj):
    print("%5s" % "", "%8s" % "Rang", "\tPutanja HTML stranice")
    for i in range(pocetak, kraj, 1):
        print("%5s" % str(i + 1) + ".","%8.2f" % lista_prikaz[i].get_rang(), lista_prikaz[i].get_stranica())


if __name__ == '__main__':

    putanja = input("Unesi putanju: ")
    ucitajPodatke(putanja)

    while (True):
        kriterijum = input("Unesite kriterijum pretrage (reci odvojene razmakom + upotreba AND,OR,NOT), X za izlazak: ")
        kriterijumArray = re.split(' ', kriterijum)
        if kriterijum == "X":
            break
        else:
            print("Kriterijum pregrate ", kriterijumArray)
            if "" in kriterijumArray:
                print("Kriterijum je prazan! Pogresan unos")
            else:
                if "OR" not in kriterijumArray and "AND" not in kriterijumArray and "NOT" not in kriterijumArray:
                    obicnaPretraga(kriterijumArray)
                    rangirana_lista = rangirajSkup(kriterijumArray)
                    paginacijaRezultata(rangirana_lista)
                elif "OR" in kriterijumArray and "AND" not in kriterijumArray and "NOT" not in kriterijumArray:
                    obicnaPretraga(kriterijumArray)
                    rangirana_lista = rangirajSkup(kriterijumArray)
                    paginacijaRezultata(rangirana_lista)
                elif "OR" not in kriterijumArray and "AND" in kriterijumArray and "NOT" not in kriterijumArray:
                    slozenijaPretraga(kriterijumArray, "AND")
                    rangirana_lista = rangirajSkup(kriterijumArray)
                    paginacijaRezultata(rangirana_lista)
                elif "OR" not in kriterijumArray and "AND" not in kriterijumArray and "NOT" in kriterijumArray:
                    slozenijaPretraga(kriterijumArray, "NOT")
                    rangirana_lista = rangirajSkup(kriterijumArray)
                    paginacijaRezultata(rangirana_lista)