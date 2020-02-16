from stack import *
import re

def infixToPostfixGenerator(kriterijum): # proveriti da li brojac dobro radi!!!
    priority = {} # recnik koji cuva prioritete
    priority["!"]= 4 # najveci prioritet
    priority["&&"] = 3
    priority["||"] = 2
    priority["("] = 1

    stek= Stack();
    result = []
    print(kriterijum)
    kriterijum= kriterijum.split()
    #print(kriterijum)
    naisaoDrugiPut= False
    brojac = 0 # ukoliko se obicna rec u kriterijumu javi vise od 1 puta znaci da imamo test1 test2 (nije navedeno || izmedju) i moramo uzeti u obrzir

    for rec in kriterijum:
        if rec== "(":
            stek.push(rec) # ako je leva zagrada ide na stek
            brojac=0
        elif rec==")":  # ako je desna zagrada uzimamo vrednost sa vrhu i sve dok ona nije "(" unosimo reci u result (svaka zatvorena mora imati svoju otvorenu)
            vrhSteka= stek.pop()
            while vrhSteka != "(":
                result.append(vrhSteka)
                vrhSteka= stek.pop()
            brojac = 0
        elif rec=="!" or rec=="&&" or rec=="||":
            while(not stek.isEmpty() and priority[stek.peek()] >= priority[rec]): # sve dok nije prazan stek i ako je prioritet u steku veci od prioriteta rec
                result.append(stek.pop()) # u result upisujemo operaciju koja ima veci prioritet
            stek.push(rec) # kada zavrsi while petlju stavlja operaciju na vrh steka
            brojac = 0
        else:
            result.append(rec) # u slucaju da naidje obicna rec(u ovom slucaju ce biti kriterijum po kojem se pretrazuje) odmah upisuje u result
            if brojac>=1:
                result.append("||")
            brojac+=1

    while not stek.isEmpty(): # sve dok nije prazan stavljamo u result sve iz steka
        result.append(stek.pop())

    return " ".join(result)



print(infixToPostfixGenerator("( dictionary list || set ) && ! tree"))
print(infixToPostfixGenerator("( dictionary list || set ) && ! tree"))
