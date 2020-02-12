from parrser import *
from trie import *
import glob

#globalne promenljive
MAPA_TRIE = {}

def ucitajTries(putanja):
    parser = Parser()
    files = glob.glob(putanja + '/**/*.html', recursive=True)
    for file in files:
        links, words = parser.parse(file)
        t = Trie()
        for word in words:
            t.add_word(word)
        MAPA_TRIE[file] = t.root

if __name__ == '__main__':
    putanja = input("Unesi putanju: ")
    ucitajTries(putanja)