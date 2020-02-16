# globalne varijable i importi

from StrukturePodataka.Graph import Graph
from StrukturePodataka.trie import *
from StrukturePodataka.Skup import *

global GRAPH
GRAPH = Graph()
global MAPA_TRIE # verovatno ce biti izbaceno
MAPA_TRIE = {}
global GLOBAL_TRIE # trie stablo koje sadrzi sve reci iz svih html dokumenata
GLOBAL_TRIE= Trie()
RESULT_SET = Skup() # skup koji sadrzi html stranice koje ispunjavaju odredjeni uslov pretrage
NADSKUP = Skup() # cuva skup svih stranica u fajlu (moze se koristiti za komplement)
global n
n = 0.05
broj_podredjenih = 0.05
global zbir_rangiranje
zbir_rangiranje = 0