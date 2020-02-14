
import glob
from Skup import *

class TrieNode():
    def __init__(self, char):
        self.char = char  # karakter u cvoru
        self.children = {}  # pokazivac na decu u cvoru
        self.endOfWord = False  # oznaka kraja reci
        self.stranice = Skup() # polje koje ima Skup stranica koje sadrze odredjenu rec i cuva broj ponavljanja date reci (file,broj_ponavljanja)

class Trie():
    def __init__(self):
        self.root = TrieNode("*")  # inicijalizacija head-a

    def add_word(self, word,file):
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)
            curr_node = curr_node.children[char]
        curr_node.endOfWord = True
        curr_node.stranice.add(file, 1) # ako stavi true da se rec zavrsila nju unosi u skup stranica, ako vec postoji u skupu kljuc file
                                        # onda ce u Skupu samo inkrementirati da se drugi put pojavila rec u datom fajlu!

    def search(self, word):

        """if word == "": # proveriti
            return "False",0, None"""

        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return "False",None
            curr_node = curr_node.children[char]

        return str(curr_node.endOfWord), curr_node.stranice

    def __bool__(self): # vraca podatak da li postoji neki unos u Trie ili ne
        return bool(self.root.char != "*" or self.root.children)

