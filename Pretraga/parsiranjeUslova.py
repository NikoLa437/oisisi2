from Ostalo import globalVar
from StrukturePodataka.Skup import Skup
from StrukturePodataka.stack import *

class TreeNode: # cvor stabla koje cemo kreirati
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isOperator(c): # proverava da li je operator && || ili !
        if (c == "&&" or c == "||" or c == "!"):
            return True
        else:
            return False

def printPostorder(root):

    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.value),

def kreirajStablo(postfix):
        stek = Stack()
        postfix = postfix.split()

        for char in postfix:

            if not isOperator(char): #  ako nije operand kreiramo cvor i stavljamo na stek
                t = TreeNode(char)
                stek.push(t)
            else:  # ako je operator
                if(char=="!"): # ako je uzvicnik kreiramo nov cvor od "!" a za levo dete stavimo vrh steka
                    t = TreeNode(char)
                    t.left = stek.pop()
                else: # ako je neki drugi operator kreiramo cvor i kao levo i desno dete stavljamo 2 stavke sa vrha steka
                    t = TreeNode(char)
                    t.right =stek.pop()
                    t.left = stek.pop()

                stek.push(t) # sta stek stavljamo cvor

        t = stek.pop() # kada prodje kroz for u steku ce se nalaziti samo root

        return t

def evaluacijaStabla(root):

    if root is None:
        return None

    if root.left is None and root.right is None:
        bool, skup = globalVar.GLOBAL_TRIE.search(root.value)
        if bool == "True":
            return skup
        else:
            return Skup()

    levo_podstablo = evaluacijaStabla(root.left)

    desno_podstablo = evaluacijaStabla(root.right)

    if root.value == "&&":
        return levo_podstablo & desno_podstablo
    elif root.value == "||":
        return levo_podstablo | desno_podstablo
    elif root.value == "!":
        return levo_podstablo.komplement(globalVar.NADSKUP)

def infixToPostfixGenerator(kriterijum): # proveriti da li brojac dobro radi!!!
    priority = {} # recnik koji cuva prioritete
    priority["!"]= 4 # najveci prioritet
    priority["&&"] = 3
    priority["||"] = 2
    priority["("] = 1

    stek= Stack();
    result = []
    #print(kriterijum)
    kriterijum= kriterijum.split()
    #print(kriterijum)
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

                                                 #ZA DULETA ! AKO TI TREBA TEST
"""postfix = infixToPostfixGenerator("( dictionary list || set ) && ! tree")
r = kreirajStablo(postfix)
printPostorder(r)"""
