def inseccion(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista1 = [7,4,5,6,43,3,2,77,8,0,1,12]
list2 = inseccion(lista1)
print(lista2)       
