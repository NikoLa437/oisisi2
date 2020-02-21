import re

def validacijaUnosaObicnaPretraga(kriterijumArray):
    if(len(kriterijumArray)>3 or "" in kriterijumArray):
        print("POGRESAN UNOS")
        print("Uneli ste vise od 2 kriterijuma pretrage")
        return False
    elif(len(kriterijumArray)==1 and (kriterijumArray[0]=="and" or kriterijumArray[0]=="or" or kriterijumArray[0]=="not")):
        print("POGRESAN UNOS")
        print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)1")
        return False
    elif(len(kriterijumArray)==2 and kriterijumArray[0] != "not" and (kriterijumArray[0]=="and" or kriterijumArray[0]=="or" or kriterijumArray[1]=="and" or kriterijumArray[1]=="or" or kriterijumArray[1]=="not")):
        print("POGRESAN UNOS")
        print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)2")
        return False
    elif(len(kriterijumArray)==2 and kriterijumArray[0]== "not" and (kriterijumArray[1]=="and" or kriterijumArray[1]=="or" or kriterijumArray[1]=="not")):
        print("POGRESAN UNOS")
        print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)3")
        return False
    elif(len(kriterijumArray)==3):
        print(kriterijumArray)
        if(kriterijumArray[0]=="and" or kriterijumArray[0]=="or" or kriterijumArray[0]=="not"):
            print("POGRESAN UNOS")
            print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)4")
            return False
        elif(kriterijumArray[2]=="and" or kriterijumArray[2]=="or" or kriterijumArray[2]=="not"):
            print("POGRESAN UNOS")
            print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)5")
            return False
        elif(kriterijumArray[1]!= "and" and kriterijumArray[1]!= "or" and kriterijumArray[1]!= "not"):
            print("POGRESAN UNOS")
            print("Uneli ste u uslov pretrage neku od rezervisanih reci za operacije(or,and,not)6")
            return False
        else:
            return True
    else:
        return True

def validacijaUnosaSlozenaPretraga(kriterijumArray):
    print(kriterijumArray)
    if kriterijumArray[0] == "||" or kriterijumArray[0] == "&&" or kriterijumArray[0]==")" or "" in kriterijumArray: # ne dozvoljava da krene sa && ili || ili )
        print("POGRESAN UNOS")
        print("Prvi i poslednji string u naprednoj pretrazi ne moze biti && ili || ili )")
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


def parsirajNapredniUnos(kriterijum):
    kriterijumArray = []
    returnValAnd = []
    returnVal = []

    kriterijumArray = re.split(' ', kriterijum.lower())

    for criteria in kriterijumArray:
        if "||" in criteria and "||" != criteria:
            podstring = criteria.split("||")
            for criteriaOR in podstring:
                if "&&" not in criteriaOR:
                    returnValAnd.append(criteriaOR)
                    if criteriaOR != podstring[len(podstring)-1]:
                        returnValAnd.append("||")
                else:
                    podstring2= criteriaOR.split("&&")
                    for criteriaAND in podstring2:
                        returnValAnd.append(criteriaAND)
                        if criteriaAND != podstring2[len(podstring2) - 1]:
                            returnValAnd.append("&&")
                        elif criteriaOR != podstring[len(podstring)-1]:
                            returnValAnd.append("||")
        elif "&&" in criteria and "&&" != criteria:
            podstring = criteria.split("&&")
            for criteriaOR in podstring:
                if "||" not in criteriaOR:
                    returnValAnd.append(criteriaOR)
                    if criteriaOR != podstring[len(podstring) - 1]:
                        returnValAnd.append("&&")
                else:
                    podstring2 = criteriaOR.split("||")
                    for criteriaAND in podstring2:
                        returnValAnd.append(criteriaAND)
                        if criteriaAND != podstring2[len(podstring2) - 1]:
                            returnValAnd.append("||")
                        elif criteriaOR != podstring[len(podstring) - 1]:
                            returnValAnd.append("&&")
        else:
            returnValAnd.append(criteria)

    for criteria in returnValAnd:
        if criteria[0]=="(" and criteria[len(criteria)-1] == ")":
            returnVal.append("(")
            returnVal.append(criteria[1:len(criteria)-2])
            returnVal.append(")")
        elif criteria[0]=="(" and criteria!="(":
            if criteria[1] == "!":
                returnVal.append("(")
                returnVal.append("!")
                returnVal.append(criteria[2:])
            else:
                returnVal.append("(")
                returnVal.append(criteria[1:])
        elif criteria[0]=="!" and criteria!="!":
            if(criteria[1]=="("):
                returnVal.append("!")
                returnVal.append("(")
                returnVal.append(criteria[2:])
            elif(criteria[1]=="!"):
                returnVal.append("!")
                returnVal.append("!")
                returnVal.append(criteria[2:])
            else:
                returnVal.append("!")
                returnVal.append(criteria[1:])
        elif criteria[len(criteria)-1] == ")" and criteria !=")":
            returnVal.append(criteria[0:len(criteria)-1])
            returnVal.append(")")
        else:
            returnVal.append(criteria)

    return returnVal
#( test && java ) && test || !(test||java)