import globalVar
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


def slozenijaPretraga(kriterijum, operacija):
    globalVar.RESULT_SET = Skup()
    RESULT_SKUP = []
    if operacija=="AND":
        for uslov in kriterijum:
            bool, skup = globalVar.GLOBAL_TRIE.search(uslov.lower())
            if bool == "True":
                RESULT_SKUP.append(skup)  # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
                globalVar.RESULT_SET= skup # postavljam bilo koji skup kao result set da posle ne bi isao prazan skup na AND operaciju!
        for file in globalVar.RESULT_SKUP:  # prolazimo kroz skup skupova html dokumenata koji ispunjavaju uslov i radimo logicko | za obicnu pretragu
            globalVar.RESULT_SET = globalVar.RESULT_SET & file  # odradjuje se or metoda nad skupovima
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
        global NADSKUP
        uslov= kriterijum[0]
        bool,skup = globalVar.GLOBAL_TRIE.search(uslov.lower())
        if bool == "True":
            globalVar.RESULT_SET = skup  # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
        globalVar.RESULT_SET= globalVar.RESULT_SET.komplement(NADSKUP)



