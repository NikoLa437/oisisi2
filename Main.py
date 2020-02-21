# from globalVar import *
import glob
import re
import sys
import time
import os

from RangiranjePaginacija import paginacija, rangiranje
from Ostalo.globalVar import GLOBAL_TRIE
from Ostalo.parrser import Parser
from Pretraga.parsiranjeUslova import infixToPostfixGenerator, kreirajStablo, evaluacijaStabla
from Pretraga.pretrage import *
from Ostalo.validacijaUnosa import *
html_list= []

"""def ucitajPodatke(putanja):
    start = time.time()
    parser = Parser()
    files = glob.glob(putanja + '/**/*.html', recursive=True)
    i = 0
    duzina = files.__len__()-1
    for file in files:
        links, words = parser.parse(file)
        globalVar.GRAPH.add_from_html(file, links)  # ===========================================================za duleta
        for word in words:
            globalVar.GLOBAL_TRIE.add_word(word.lower(), file)
        globalVar.NADSKUP.add(file, 0)
        #update_progress(round(i/duzina,4))
        i+=1
    end = time.time()
    print(end - start)"""

"""def ucitajPodatke(putanja):
    start = time.time()
    parser = Parser()
    i = 0
    for root, dirs, files in os.walk(putanja):
        #duzina = files.__len__()-1
        for file in files:
            if (file.endswith('html')):
                f= root+ "\\" + file
                links, words = parser.parse(f)
                globalVar.GRAPH.add_from_html(f, links)  # ===========================================================za duleta
                for word in words:
                    globalVar.GLOBAL_TRIE.add_word(word.lower(), f)
                globalVar.NADSKUP.add(f, 0)
                #update_progress(round(i/duzina,4))
                #i+=1
    end = time.time()
    print(end - start)"""

def ucitajPodatke(putanja):
    parser = Parser()
    #prodji(putanja)
    #i = 0
    #duzina = html_list.__len__() - 1
    for path in prodji(putanja):
        links, words = parser.parse(path)
        globalVar.GRAPH.add_from_html(path, links)  # ===========================================================za duleta
        for word in words:
            globalVar.GLOBAL_TRIE.add_word(word.lower(), path)
        globalVar.NADSKUP.add(path, 0)
        #update_progress(round(i/duzina,4))
        #i+=1

def update_progress(progress):
    barLength = 100 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(barLength*progress)
    text = "\rLoading: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), round(progress*100,2), status)
    sys.stdout.write(text)
    sys.stdout.flush()

#funkcija za pronalazak html fajlova
def prodji(putanja):
    dirs = os.listdir(putanja)
    for dir in dirs:
        if os.path.isdir(putanja + "\\" + dir):
            prodji(putanja + "\\" + dir)
        else:
            if dir.endswith(".html"):
                html_list.append(putanja + "\\" + dir)
    return html_list

if __name__ == '__main__':

    print(sys.platform)
    while True:
        putanja = input("Unesi putanju(X za izlaz): ")
        start= time.time()
        ucitajPodatke(putanja)
        end = time.time()
        print(end-start)
        if putanja == "X":
            sys.exit()
        elif not bool(GLOBAL_TRIE):
            print("Nije ucitan nijedan fajl! Uneli ste pogresnu apsolutnu adresu ili u datoteci nema html fajlova (X za izlaz)")
        else:
            break

    kriterijumArray = []

    while (True):
        print("Odaberite vrstu pretrage:")
        print("1 - Obicna pretraga")
        print("2 - Napredna pretraga")
        print("X - Izlaz iz programa")
        nacin_pretrage = input("Unos: ")
        if nacin_pretrage == "1":
            while(True):
                kriterijum = input("Unesite kriterijum pretrage (reci odvojene razmakom + upotreba AND,OR,NOT), X za izlazak: ")
                kriterijumArray = re.split(' ', kriterijum.lower())
                if kriterijum == "X":
                    break
                else:
                    if validacijaUnosaObicnaPretraga(kriterijumArray):
                        br_pod = input(
                            "Unesite broj podredjenih cvorova koji zelite da utice na rangiranje (sto je broj veci to "
                            "ce rangiranje biti sporije): ")
                        globalVar.broj_podredjenih = 0.300001 / (3 ** (float(br_pod) - 1))
                        globalVar.n = globalVar.broj_podredjenih
                        if "or" not in kriterijumArray and "and" not in kriterijumArray and "not" not in kriterijumArray:
                            slozenijaPretraga(kriterijumArray, "OR")
                            start = time.time()
                            rangirana_lista = rangiranje.rangirajSkup(kriterijumArray)
                            stop = time.time();
                            print(stop - start)
                            paginacija.paginacijaRezultata(rangirana_lista)
                        elif "or" in kriterijumArray and "and" not in kriterijumArray and "not" not in kriterijumArray:
                            kriterijumArray.remove("or")
                            slozenijaPretraga(kriterijumArray, "OR")
                            rangirana_lista = rangiranje.rangirajSkup(kriterijumArray)
                            paginacija.paginacijaRezultata(rangirana_lista)
                        elif "or" not in kriterijumArray and "and" in kriterijumArray and "not" not in kriterijumArray:
                            kriterijumArray.remove("and")
                            slozenijaPretraga(kriterijumArray, "AND")
                            rangirana_lista = rangiranje.rangirajSkup(kriterijumArray)
                            paginacija.paginacijaRezultata(rangirana_lista)
                        elif "or" not in kriterijumArray and "and" not in kriterijumArray and kriterijumArray[0] == "not":
                            kriterijumArray.remove("not")
                            slozenijaPretraga(kriterijumArray, "KOMPLEMENT")
                            rangirana_lista = rangiranje.rangirajSkup(kriterijumArray)
                            paginacija.paginacijaRezultata(rangirana_lista)
                        elif "or" not in kriterijumArray and "and" not in kriterijumArray and "not" in kriterijumArray:
                            kriterijumArray.remove("not")
                            slozenijaPretraga(kriterijumArray, "NOT")
                            rangirana_lista = rangiranje.rangirajSkup(kriterijumArray)
                            paginacija.paginacijaRezultata(rangirana_lista)
        elif nacin_pretrage == "2":
            while True:
                kriterijum = input("Unesite kriterijum napredne pretrage ili X za izlazak: ")
                kriterijumArray = parsirajNapredniUnos(kriterijum)
                print(kriterijumArray)
                if kriterijum != "X":
                    if validacijaUnosaSlozenaPretraga(kriterijumArray):
                        br_pod = input(
                            "Unesite broj podredjenih cvorova koji zelite da utice na rangiranje (sto je broj veci to "
                            "ce rangiranje biti sporije): ")
                        globalVar.broj_podredjenih = 0.300001 / (3 ** (float(br_pod) - 1))
                        globalVar.n = globalVar.broj_podredjenih
                        postfix = infixToPostfixGenerator(kriterijumArray)
                        root = kreirajStablo(postfix)
                        globalVar.RESULT_SET = evaluacijaStabla(root)
                        if "&&" in kriterijumArray:
                            kriterijumArray.remove("&&")
                        if "||" in kriterijumArray:
                            kriterijumArray.remove("||")
                        if "!" in kriterijumArray:
                            kriterijumArray.remove("!")
                        if ")" in kriterijumArray:
                            kriterijumArray.remove(")")
                        if "(" in kriterijumArray:
                            kriterijumArray.remove("(")
                        rangirana_lista = rangiranje.rangirajSkup(kriterijumArray)
                        paginacija.paginacijaRezultata(rangirana_lista)
                else:
                    break
        elif nacin_pretrage == "X" or nacin_pretrage == "x":
            sys.exit()
            #( test && java ) && ! test || !(test||java)
