from Ostalo import globalVar
from StrukturePodataka.Skup import Skup

def slozenijaPretraga(kriterijum, operacija):
    globalVar.RESULT_SET = Skup()
    smestena_prva = False
    RESULT_SKUP = []
    drugi_skup = Skup()
    if operacija =="OR":
        for uslov in kriterijum:
            bool, skup = globalVar.GLOBAL_TRIE.search(uslov.lower())  # dobijamo skup pretrage
            if bool == "True": # ako postoji skup
                RESULT_SKUP.append(skup) # ostale skupove dodajemo
        for file in RESULT_SKUP:  # prolazimo kroz skup skupova html dokumenata koji ispunjavaju uslov i radimo logicko | za obicnu pretragu
            globalVar.RESULT_SET = globalVar.RESULT_SET | file
    elif operacija=="AND":
        for uslov in kriterijum:
            bool, skup = globalVar.GLOBAL_TRIE.search(uslov.lower())  # dobijamo skup pretrage
            if bool == "True": # ako postoji skup
                if not smestena_prva: # ako nismo smestili prvi
                    globalVar.RESULT_SET= skup # postavljam bilo koji skup kao result set da posle ne bi isao prazan skup na AND operaciju!
                    smestena_prva = True
                else:
                    drugi_skup = skup # drugi skup za operaciju &
        globalVar.RESULT_SET = globalVar.RESULT_SET & drugi_skup  # odradjuje se or metoda nad skupovima
    elif operacija=="NOT":
        smestena_prva= False
        for uslov in kriterijum:
            bool, skup = globalVar.GLOBAL_TRIE.search(uslov.lower())
            if bool == "True":
                globalVar.RESULT_SKUP.append(skup)  # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
                if not smestena_prva:
                    globalVar.RESULT_SET= skup # postavljam bilo koji skup kao result set da posle ne bi isao prazan skup na AND operaciju!
                    smestena_prva=True
                else:
                    drugi_skup = skup
        globalVar.RESULT_SET = globalVar.RESULT_SET - drugi_skup  # odradjuje se or metoda nad skupovima
    elif operacija=="KOMPLEMENT":
        uslov= kriterijum[0]
        bool,skup = globalVar.GLOBAL_TRIE.search(uslov.lower())
        if bool == "True":
            globalVar.RESULT_SET = skup  # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
        globalVar.RESULT_SET= globalVar.RESULT_SET.komplement(globalVar.NADSKUP)



