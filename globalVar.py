# globalne varijable i importi

import copy
import time
import rangiranje
from parrser import *
from trie import *
import glob
import os
from Skup import *
from Graph import Graph
import re
import sys

global GRAPH
GRAPH = Graph()
global MAPA_TRIE # verovatno ce biti izbaceno
MAPA_TRIE = {}
global GLOBAL_TRIE # trie stablo koje sadrzi sve reci iz svih html dokumenata
GLOBAL_TRIE= Trie()
RESULT_SET = Skup() # skup koji sadrzi html stranice koje ispunjavaju odredjeni uslov pretrage
RESULT_SKUP = [] # globalna koja sluzi da cuva skup skupova koje treba porediti po AND OR NOT operatorima
NADSKUP = Skup() # cuva skup svih stranica u fajlu (moze se koristiti za komplement)