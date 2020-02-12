
import glob

class TrieNode():
    def __init__(self, char):
        self.char = char  # karakter u cvoru
        self.children = {}  # pokazivac na decu u cvoru
        self.endOfWord = False  # oznaka kraja reci
        self.counter = 0  # brojac pojavljivanja reci


class Trie():
    def __init__(self):
        self.root = TrieNode("*")  # inicijalizacija head-a

    def add_word(self, word):
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)
            curr_node = curr_node.children[char]

        curr_node.endOfWord = True
        curr_node.counter += 1

    def search(self, word):
        if word == "":
            return True

        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return curr_node.endOfWord, curr_node.counter

