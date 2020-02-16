def mergeSort(lista_prikaza):
    if len(lista_prikaza) > 1:
        mid = len(lista_prikaza) // 2  # trazenje sredine niza
        L = lista_prikaza[:mid]  # deljenje elemenata liste
        R = lista_prikaza[mid:]  # na 2 polovine

        mergeSort(L)  # sortiranje prve polovine
        mergeSort(R)  # sortiranje druge polovine

        i = j = k = 0

        # kopiranje podataka u privremene nizove L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].get_rang() > R[j].get_rang():
                lista_prikaza[k] = L[i]
                i += 1
            else:
                lista_prikaza[k] = R[j]
                j += 1
            k += 1

        # provera da li je ostao neki element
        while i < len(L):
            lista_prikaza[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista_prikaza[k] = R[j]
            j += 1
            k += 1