class Skup:
    def __init__(self):
        self._stranice = {}

    def add(self, stranica):
        if not self.__contains__(stranica):
            self._stranice[stranica] = stranica

    def remove(self, stranica):
        if self.__contains__(stranica):
            del self._stranice[stranica]

    def __contains__(self, item):
        return self._stranice.keys().__contains__(item)

    def __iter__(self):
        return iter(self._stranice.copy())

    def __or__(self, other):

        retVal = Skup()
        for e in other:
            retVal.add(e)
        for s in self:
            retVal.add(s)

        return retVal

    def __and__(self, other):

        retVal = Skup()

        for e in other:
            if self.__contains__(e):
                retVal.add(e)
        return retVal

    def __sub__(self, other):

        retVal = Skup()

        for e in self:
            if not other.__contains__(e):
                retVal.add(e)
        return retVal

    def komplement(self, nadskup):

        retVal = Skup()

        for e in nadskup:
            if not self.__contains__(e):
                retVal.add(e)

        return retVal