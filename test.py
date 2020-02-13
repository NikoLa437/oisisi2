from parrser import *
from trie import *
import glob
import time
import os
import re # za split

#globalne promenljive
MAPA_TRIE = {}
RESULT_SETS = []

def ucitajTries(putanja):
    start=time.time()
    parser= Parser()
    for root, dirs, files in os.walk("python-2.7.7-docs-html/howto"):
        for file in files:
            if file.endswith('.html'):
                links, words = parser.parse(os.path.join(root, file))
                #t = Trie()
                #for word in words:
                #    t.add_word(word)
                #    MAPA_TRIE[file] = t.root
    end = time.time()
    print(end-start)

def obicnaPretraga(kriterijum):
    for uslov in kriterijum:
        skup= Skup()
        for trie in MAPA_TRIE.values():
            boo, pojavlj



if __name__ == '__main__':
    putanja = input("Unesi putanju: ")
    ucitajTries(putanja)

    kriterijum = input("Unesite kriterijum pretrage (reci odvojene razmakom + upotreba AND,OR,NOT), X za izlazak: ")

    while(True):
        if kriterijum=="X":
            break
        else:
            kriterijumArray= re.split(' ',kriterijum)
            if "OR" not in kriterijumArray and "AND" not in kriterijumArray and "NOT" not in kriterijumArray:
                print("test")
            break