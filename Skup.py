class Skup:
    def __init__(self):
        self._stranice = {}

    def add(self, stranica,broj):
        if not self.__contains__(stranica):
            self._stranice[stranica] = broj  # inicijalizuje ukoliko nema stranice na broj pojavljivanja date reci
        else:
            self._stranice[stranica] +=1 # ukoliko vec postoji u datom html fajlu data rec samo povecava njen broj

    def getStr(self):
        return self._stranice # vraca stranice,koristimo da bi mogli da dobijemo vrednost recnika u uniji,preseku,komplementu

    def remove(self, stranica):
        if self.__contains__(stranica):
            del self._stranice[stranica]

    def __contains__(self, item):
        return self._stranice.keys().__contains__(item)

    def __iter__(self):
        return iter(self._stranice.copy())

    def __or__(self, other):

        retVal = Skup()
        for s in other:
            o=other.getStr()
            retVal.add(s,o[s])
        for s in self:
            retVal.add(s,self._stranice[s])
        return retVal


    def __and__(self, other):

        retVal = Skup()

        for e in other:
            if self.__contains__(e):
                retVal.add(e,self._stranice[e])

        return retVal

    def __sub__(self, other):

        retVal = Skup()

        for e in self:
            if not other.__contains__(e):
                retVal.add(e,self._stranice[e])
        return retVal

    def komplement(self, nadskup):

        retVal = Skup()

        for e in nadskup:
            o = nadskup.getStr()
            if not self.__contains__(e):
                retVal.add(e,o[e])

        return retVal