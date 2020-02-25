def paginacijaRezultata(lista_prikaz):
    N = 10
    pocetak = 0
    duzina = len(lista_prikaz)
    if duzina != 0:
        if N > duzina:
            kraj = duzina
            N = kraj
        else:
            kraj = N
        while (True):
            ispisiRezultate(lista_prikaz, pocetak, kraj)
            print("\n")
            print("Izaberite opciju:")
            print("1 - Za prikaz sledecih " + str(N) + " stranica")
            print("2 - Za prikaz prethodnih " + str(N) + " stranica")
            print("3 - Za promenu broja prikazanih stranica")
            print("X - Za izlazak iz prikaza")
            izbor = input("Unesite opciju: ")

            if izbor == "X" or izbor == "x":
                break
            if izbor == "1":
                if kraj + N > duzina:
                    """if len(lista_prikaz) - N < 0:
                        pocetak = 0
                    else:
                        pocetak = kraj"""
                    if pocetak + N < duzina:
                        pocetak += N
                    kraj = duzina
                else:
                    kraj += N
                    pocetak += N
            if izbor == "2":
                if pocetak - N < 0:
                    pocetak = 0
                    if N > duzina:
                        kraj = duzina
                    else:
                        kraj = N
                else:
                    kraj = pocetak
                    pocetak -= N

            if izbor == "3":
                n = input("Unesite trazeni broj (broj mora biti veci od 1, ako se pogresno unese po defaultu ce biti 10): ")
                if not n.isdigit():
                    n = 10
                if int(n) <= 0:
                    n = 10
                N = int(n)
                if N > duzina:
                    N = duzina
                    print("Unet veci broj od broja stranica")
                if pocetak + N > duzina:
                    kraj = duzina
                else:
                    kraj = pocetak + N
    else:
        print("Ne postoje HTML stranice koje zadovoljavaju zadati kriterijum!")

def ispisiRezultate(lista_prikaz, pocetak, kraj):
    print("%5s" % "", "%8s" % "Rang", "\tPutanja HTML stranice")
    for i in range(pocetak, kraj, 1):
        print("%5s" % str(i + 1) + ".", "%8.2f" % lista_prikaz[i].get_rang(), lista_prikaz[i].get_stranica())
    if(kraj == len(lista_prikaz)):
        print("Dosli ste do kraja!")