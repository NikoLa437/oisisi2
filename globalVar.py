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
global MAPA_TRIE
MAPA_TRIE = {}
global GLOBAL_TRIE
GLOBAL_TRIE= Trie()
RESULT_SET = Skup()
RESULT_SKUP = []