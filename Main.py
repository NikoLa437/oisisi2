# from globalVar import *
import copy
import glob
import re
import sys
import time

import rangiranje
from globalVar import GRAPH, GLOBAL_TRIE, NADSKUP
from mergeSort import mergeSort
from parrser import Parser
from pretrage import *

#broj_podredjenih = 0.05

def ucitajPodatke(putanja):
    start = time.time()
    parser = Parser()
    files = glob.glob(putanja + '/**/*.html', recursive=True)
    for file in files:
        links, words = parser.parse(file)
        GRAPH.add_from_html(file, links)  # ===========================================================za duleta
        for word in words:
            GLOBAL_TRIE.add_word(word.lower(), file)
            NADSKUP.add(file, 0)
    end = time.time()
    print(end - start)


# cuvam za svaki slucaj sa os.walk
"""
for root, dirs, files in os.walk(putanja):
        for file in files:
            if file.endswith('.html'):
                links, words = parser.parse(os.path.join(root, file))
                t = Trie()
                GRAPH.add_from_html(os.path.join(root, file), links)
                for word in words:
                    t.add_word(word.lower())
                    MAPA_TRIE[os.path.join(root, file)] = t
"""


def rangirajSkup(niz_reci):

    retVal = [] # lista koja ce kasnije biti ispisana

    mapa_prikaza = rangiranje.prvo_rangiranje(niz_reci)  # prvo rangiranje - po broju reci u stranicama- svaka rec +=
                                                         # 0.5 u rangu
    nova_mapa = copy.deepcopy(mapa_prikaza) # radimo deep copy mape [stanica, rang], da bi na sledece rangiranje
                                            # uticalo prethodno stanje
                                            # (onemogucavamo da se dinamicki menja tokom rangiranja)

    # rangiranje na osnovu broja reci linkovanim stranicama, na osnovu broja (0.3) odredjujemo "dubinu" rangiranja
    for el in mapa_prikaza:
        mapa_prikaza[el] += rangiranje.drugo_rangiranje(nova_mapa, GRAPH.get_incoming(el), 0.3, GRAPH)
        mapa_prikaza[el] += globalVar.zbir_rangiranje
        globalVar.zbir_rangiranje = 0
        globalVar.n = 0.05

    del nova_mapa #vise nam nije potrebna
    # rangiranje na osnovu broja linkova
    for el in mapa_prikaza:
        mapa_prikaza[el] = mapa_prikaza[el] + GRAPH.get_incoming(el).__len__()

    for el in mapa_prikaza:
        retVal.append(rangiranje.Prikaz(el, mapa_prikaza[el]))

    mergeSort(retVal) # sortiramo rezultat
    return retVal


def paginacijaRezultata(lista_prikaz):
    N = 10
    pocetak = 0
    if N > len(lista_prikaz):
        kraj = len(lista_prikaz)
    else:
        kraj = N
    while (True):
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
            if kraj + N > len(lista_prikaz):
                if pocetak - N < 0:
                    pocetak = 0
                else:
                    pocetak = kraj
                kraj = len(lista_prikaz)
            else:
                kraj += N
                pocetak += N
        if izbor == "2":
            if pocetak - N < 0:
                pocetak = 0
                if N > len(lista_prikaz):
                    kraj = len(lista_prikaz)
                else:
                    kraj = N
            else:
                kraj = pocetak
                pocetak -= N

        if izbor == "3":
            n = input("Unesite trazeni broj:")
            N = int(n)
            if pocetak + N > len(lista_prikaz):
                kraj = len(lista_prikaz)
            else:
                kraj = pocetak + N


def ispisiRezultate(lista_prikaz, pocetak, kraj):
    print("%5s" % "", "%8s" % "Rang", "\tPutanja HTML stranice")
    for i in range(pocetak, kraj, 1):
        print("%5s" % str(i + 1) + ".", "%8.2f" % lista_prikaz[i].get_rang(), lista_prikaz[i].get_stranica())


if __name__ == '__main__':
    while (True):
        putanja = input("Unesi putanju(X za izlaz): ")
        ucitajPodatke(putanja)
        """br_pod = input("Unesite broj podredjenih cvorova koji zelite da utice na rangiranje: ")
        broj_podredjenih = 0.300001 / float(br_pod)
        globalVar.n = broj_podredjenih"""
        if putanja == "X":
            sys.exit()
        elif not bool(GLOBAL_TRIE):
            print(
                "Nije ucitan nijedan fajl! Uneli ste pogresnu apsolutnu adresu ili u datoteci nema html fajlova (X za izlaz)")
        else:
            break

    kriterijumArray = []

    while (True):
        kriterijum = input("Unesite kriterijum pretrage (reci odvojene razmakom + upotreba AND,OR,NOT), X za izlazak: ")
        kriterijumArray = re.split(' ', kriterijum.lower())
        if kriterijum == "X":
            sys.exit()
        else:
            print("Kriterijum pregrate ", kriterijumArray)
            if "" in kriterijumArray:
                print("Kriterijum je prazan! Pogresan unos")
            else:
                if "or" not in kriterijumArray and "and" not in kriterijumArray and "not" not in kriterijumArray:
                    obicnaPretraga(kriterijumArray)
                    start = time.time()
                    rangirana_lista = rangirajSkup(kriterijumArray)
                    stop = time.time();
                    print(stop - start)
                    paginacijaRezultata(rangirana_lista)
                elif "or" in kriterijumArray and "and" not in kriterijumArray and "not" not in kriterijumArray:
                    kriterijumArray.remove("or")
                    obicnaPretraga(kriterijumArray)
                    # rangirana_lista = rangirajSkup(kriterijumArray)
                    # paginacijaRezultata(rangirana_lista)
                elif "or" not in kriterijumArray and "and" in kriterijumArray and "not" not in kriterijumArray:
                    kriterijumArray.remove("and")
                    slozenijaPretraga(kriterijumArray, "AND")
                    # rangirana_lista = rangirajSkup(kriterijumArray)
                    # paginacijaRezultata(rangirana_lista)
                elif "or" not in kriterijumArray and "and" not in kriterijumArray and kriterijumArray[0] == "not":
                    kriterijumArray.remove("not")
                    slozenijaPretraga(kriterijumArray, "KOMPLEMENT")
                elif "or" not in kriterijumArray and "and" not in kriterijumArray and "not" in kriterijumArray:
                    kriterijumArray.remove("not")
                    slozenijaPretraga(kriterijumArray, "NOT")
                    # rangirana_lista = rangirajSkup(kriterijumArray)
                    # paginacijaRezultata(rangirana_lista)
