
import glob
from Skup import *

class TrieNode():
    def __init__(self, char):
        self.char = char  # karakter u cvoru
        self.children = {}  # pokazivac na decu u cvoru
        self.endOfWord = False  # oznaka kraja reci
        self.counter = 0  # brojac pojavljivanja reci
        self.stranice = Skup()

class Trie():
    def __init__(self):
        self.root = TrieNode("*")  # inicijalizacija head-a

    def add_word(self, word,file):
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)
            curr_node = curr_node.children[char]
        curr_node.counter+=1
        curr_node.endOfWord = True
        curr_node.stranice.add(file, 1)

    def search(self, word):
        if word == "":
            return "False",0, None

        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return "False",0,None
            curr_node = curr_node.children[char]

        return str(curr_node.endOfWord),0, curr_node.stranice

