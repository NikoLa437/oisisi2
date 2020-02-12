import time
import rangiranje
from parrser import *
from trie import *
import glob
from Graph import Graph

global graph
graph = Graph()
global MAPA_TRIE
MAPA_TRIE = {}

"""
def ucitajTries(putanja):
    parser = Parser()
    files = glob.glob(putanja + '/**/*.html', recursive=True)
    for file in files:
        links, words = parser.parse(file)
        t = Trie()
        for word in words:
            t.add_word(word)
        globalVars.MAPA_TRIE[file] = t.root
"""


def ucitajTries(words):
    t = Trie()
    for word in words:
        t.add_word(word)
    MAPA_TRIE[file] = t.root


if __name__ == '__main__':


    putanja = input("Unesi putanju: ")
    # ucitajTries(putanja)
    parserr = Parser()
    files = glob.glob(putanja + '/**/*.html', recursive=True)

    start = time.time()
    for file in files:
        links, words = parserr.parse(file)
        graph.add_from_html(file, links)
        ucitajTries(words)

    end = time.time()
    print(end - start)

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
