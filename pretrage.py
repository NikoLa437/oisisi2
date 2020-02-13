from globalVar import *

def obicnaPretraga(kriterijum):
    global RESULT_SET
    RESULT_SET= Skup()
    for uslov in kriterijum:
        skup = Skup()
        for key in MAPA_TRIE:
            bool, ponavaljanja = MAPA_TRIE[key].search(uslov.lower())
            if bool == "True":
                skup.add(key) # dodaje u skup sve html dokumente koji sadrze datu rec
        RESULT_SKUP.append(skup) # niz skupova koji sadrze html dokumente koji ispunjavaju uslov
    for file in RESULT_SKUP:  # prolazimo kroz skup skupova html dokumenata koji ispunjavaju uslov i radimo logicko | za obicnu pretragu
        RESULT_SET = RESULT_SET | file


def slozenijaPretraga(kriterijum, operacija):
    print("Test: ", operacija)