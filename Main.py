import time
#import rangiranje
from parrser import *
from trie import *
import glob
import os
from Skup import *
from Graph import Graph
import re

global graph
GRAPH = Graph()
global MAPA_TRIE
MAPA_TRIE = {}
RESULT_SET = Skup()
RESULT_SKUP = []

def ucitajPodatke(putanja):
    start=time.time()
    parser= Parser()
    for root, dirs, files in os.walk("python-2.7.7-docs-html"):
        for file in files:
            if file.endswith('.html'):
                links, words = parser.parse(os.path.join(root, file))
                t = Trie()
                GRAPH.add_from_html(file, links)
                for word in words:
                    t.add_word(word.lower())
                    MAPA_TRIE[os.path.join(root, file)] = t
    end = time.time()
    print(end-start)

def obicnaPretraga(kriterijum):
    for uslov in kriterijum:
        skup = Skup()
        for key in MAPA_TRIE:
            bool, ponavaljanja = MAPA_TRIE[key].search(uslov)
            if bool=="True":
                skup.add(key)
        RESULT_SKUP.append(skup)

if __name__ == '__main__':

    putanja = input("Unesi putanju: ")
    ucitajPodatkes(putanja)
    kriterijum = input("Unesite kriterijum pretrage (reci odvojene razmakom + upotreba AND,OR,NOT), X za izlazak: ")
    kriterijumArray = re.split(' ', kriterijum)

    while (True):
        if kriterijum == "X":
            break
        else:
            if "OR" not in kriterijumArray and "AND" not in kriterijumArray and "NOT" not in kriterijumArray:
                obicnaPretraga(kriterijumArray)
                RESULT_SET=Skup()
                for file in RESULT_SKUP:
                    RESULT_SET = RESULT_SET | file
                for file in RESULT_SET:
                    print(file)

            break














    """mapa_prikaza = {}

    for cvor in graph.vertices():
        prikaz = rangiranje.prvo_rangiranje(cvor, MAPA_TRIE[cvor],
                                                                   graph.get_incoming(cvor).__len__())
        mapa_prikaza[prikaz.get_stranica()] = prikaz.get_rang()
    print("RANGIRANJE 1\n\n\n")
    for el in mapa_prikaza:
        print(el, "   rang:", mapa_prikaza[el])

    i = 0
    print("\n\n\nRANGIRANJE 2\n\n\n")
    nova_mapa = {}

    for m in mapa_prikaza:
        nova_mapa[m] = mapa_prikaza[m]

    for el in mapa_prikaza:
        mapa_prikaza[el] = rangiranje.drugo_rangiranje(nova_mapa[el],mapa_prikaza,graph.get_incoming(el), 0.5)
        if i == 0:
            for v in graph.get_incoming(el):
                print(v, "rang linkova", mapa_prikaza[v])
        i+=1

    for el in mapa_prikaza:
        print(el, "   rang:", mapa_prikaza[el])"""
