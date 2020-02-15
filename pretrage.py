import globalVar
#from globalVar import *
from Skup import Skup


def obicnaPretraga(kriterijum):
    globalVar.RESULT_SET = Skup() ################### ZA DZONIJA - ovako pristupaj globalnim, u mainu izgleda ne mora, za GRAPH i GLOBAL_TRIE bude okej zato sto se tamo dodaje
    RESULT_SKUP= []
    for uslov in kriterijum:
            bool, skup = globalVar.GLOBAL_TRIE.search(uslov.lower())
            if bool=="True":
                RESULT_SKUP.append(skup) # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
    for file in RESULT_SKUP:  # prolazimo kroz skup skupova html dokumenata koji ispunjavaju uslov i radimo logicko | za obicnu pretragu
        globalVar.RESULT_SET = globalVar.RESULT_SET | file # odradjuje se or metoda nad skupovima
    """for f in RESULT_SET:
        print(f)"""


def slozenijaPretraga(kriterijum, operacija):
    global RESULT_SET
    RESULT_SET = Skup()
    RESULT_SKUP = []
    if operacija=="AND":
        for uslov in kriterijum:
            bool, skup = globalVar.GLOBAL_TRIE.search(uslov.lower())
            if bool == "True":
                RESULT_SKUP.append(skup)  # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
                RESULT_SET= skup # postavljam bilo koji skup kao result set da posle ne bi isao prazan skup na AND operaciju!
        for file in RESULT_SKUP:  # prolazimo kroz skup skupova html dokumenata koji ispunjavaju uslov i radimo logicko | za obicnu pretragu
            RESULT_SET = RESULT_SET & file  # odradjuje se or metoda nad skupovima
        """for f in RESULT_SET:
            print(f)"""
    elif operacija=="NOT":
        smestena_prva= False
        for uslov in kriterijum:
            bool, skup = globalVar.GLOBAL_TRIE.search(uslov.lower())
            if bool == "True":
                RESULT_SKUP.append(skup)  # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
                if not smestena_prva:
                    RESULT_SET= skup # postavljam bilo koji skup kao result set da posle ne bi isao prazan skup na AND operaciju!
                    smestena_prva=True
                else:
                    drugi_skup = skup

        RESULT_SET = RESULT_SET - drugi_skup  # odradjuje se or metoda nad skupovima
        """for f in RESULT_SET:
            print(f)"""
    elif operacija=="KOMPLEMENT":
        global NADSKUP
        uslov= kriterijum[0]
        bool,skup = globalVar.GLOBAL_TRIE.search(uslov.lower())
        if bool == "True":
            RESULT_SET = skup  # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
        RESULT_SET= RESULT_SET.komplement(NADSKUP)
        """for f in RESULT_SET:
            print(f)"""



