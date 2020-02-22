import re

def validacijaUnosaObicnaPretraga(kriterijumArray):
    if "" in kriterijumArray:
        print("POGRESAN UNOS!")
        print("Uneli ste prazan string u pretragu")
        print("FORMAT: Uslov1 OPERATOR Uslov2 | NOT Uslov1 | Uslov1 Uslov2 Uslov3 ... UslovN")
        return False
    elif(len(kriterijumArray)==1 and (kriterijumArray[0]=="and" or kriterijumArray[0]=="or" or kriterijumArray[0]=="not")):
        print("POGRESAN UNOS")
        print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)")
        print("FORMAT: Uslov1 OPERATOR Uslov2 | NOT Uslov1 | Uslov1 Uslov2 Uslov3 ... UslovN")
        return False
    elif(len(kriterijumArray)==2 and (kriterijumArray[0]=="and" or kriterijumArray[0]=="or" or kriterijumArray[1]=="and" or kriterijumArray[1]=="or" or kriterijumArray[1]=="not")):
        print("POGRESAN UNOS")
        print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)")
        print("FORMAT: Uslov1 OPERATOR Uslov2 | NOT Uslov1 | Uslov1 Uslov2 Uslov3 ... UslovN")
        return False
    elif(len(kriterijumArray)==3):
        print(kriterijumArray)
        if(kriterijumArray[0]=="and" or kriterijumArray[0]=="or" or kriterijumArray[0]=="not"):
            print("POGRESAN UNOS")
            print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)")
            print("FORMAT: Uslov1 OPERATOR Uslov2 | NOT Uslov1 | Uslov1 Uslov2 Uslov3 ... UslovN")
            return False
        elif(kriterijumArray[2]=="and" or kriterijumArray[2]=="or" or kriterijumArray[2]=="not"):
            print("POGRESAN UNOS")
            print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)")
            print("FORMAT: Uslov1 OPERATOR Uslov2 | NOT Uslov1 | Uslov1 Uslov2 Uslov3 ... UslovN")
            return False
        else:
            return True
    elif len(kriterijumArray)>3:
        if "or" in kriterijumArray or "and" in kriterijumArray or "not" in kriterijumArray:
            print("POGRESAN UNOS")
            print("Uneli ste kriterijum pretrage sa vise od 2 uslova pri cemu ste koristili operator")
            print("FORMAT: Uslov1 OPERATOR Uslov2 | NOT Uslov1 | Uslov1 Uslov2 Uslov3 ... UslovN")
            return False
        else:
            return True
    else:
        return True

def validacijaUnosaSlozenaPretraga(kriterijumArray):
    print(kriterijumArray)
    if kriterijumArray[0] == "||" or kriterijumArray[0] == "&&" or kriterijumArray[0]==")" or "" in kriterijumArray: # ne dozvoljava da krene sa && ili || ili )
        print("POGRESAN UNOS")
        print("Prvi i poslednji string u naprednoj pretrazi ne moze biti && , || , ) ili imate prazan string kao kriterijum")
        return False
    elif kriterijumArray[len(kriterijumArray)-1] == "||" or kriterijumArray[len(kriterijumArray)-1] == "!" or kriterijumArray[len(kriterijumArray)-1] == "&&" or kriterijumArray[len(kriterijumArray)-1] == "(":
        print("POGRESAN UNOS") # ne dozvoljava da se pretraga zavrsava sa || && ili !
        print("Prvi i poslednji string u naprednoj pretrazi ne moze biti && ili || ili (")
        return False
    elif kriterijumArray.count("(") != kriterijumArray.count(")"): # broj otvorenih i zatvorenih zagrada mora biti isti
        print("POGRESAN UNOS")
        print("Broj ( mora biti jednak broju ) u izrazu")
        return False
    else:
        prolaz = True
        operators= ["&&" , "||" , "!"]
        operators2 = ["&&" ,"||"]
        for i in range(0,len(kriterijumArray)-1):
            if(kriterijumArray[0]=="!" and (kriterijumArray[1] == "||" or kriterijumArray[1] =="&&")):
                print("POGRESAN UNOS")
                print("Ukoliko je prvi string ! drugi ne sme biti || ili &&")
                prolaz=False
                break
            elif(kriterijumArray[i] in operators2 and kriterijumArray[i+1] in operators2):
                print("POGRESAN UNOS")
                print("Nakon && ili || ili ! ne sme ici && ili ||")
                prolaz = False
                break
            elif(kriterijumArray[i] == "!" and kriterijumArray[i+1] in operators):
                print("POGRESAN UNOS")
                print("Nakon ! ne sme ici && , || ili !")
                prolaz = False
                break
            elif(kriterijumArray[i] == "(" and (kriterijumArray[i+1] == "&&" or kriterijumArray[i+1] == "||" or kriterijumArray[i+1] == ")")):
                print("POGRESAN UNOS")
                print("Nakon ( ne sme ici && , || , ( ili )")
                prolaz = False
                break
            elif (kriterijumArray[i+1] == ")" and ( kriterijumArray[i] in operators or kriterijumArray[i] == ")")):
                print("POGRESAN UNOS")
                print("Pre ) ne sme ici && , || , ! , ( ili )")
                prolaz = False
                break

        return prolaz

#( test && java ) && test || !(test||java)