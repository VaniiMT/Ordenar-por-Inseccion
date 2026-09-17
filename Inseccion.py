def inseccion(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista1 = [7,4,5,6,43,3,2,77,8,0,1,12]
list2 = inseccion(lista1)
print(lista2)       

#for i = N-1 to 1:
    #if A[i] < A[i-1], then swap A[i] and A[i-1]
    #else stop

def inseccion1(lista):  #NO FUNCIONA
    for i in range(1, len(lista)):
        j = i - 1
        while j >= 0 and lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            j -= 1
    return lista

lista1 = [7,4,5,6,43,3,2,77,8,0,1,12]
lista3 = inseccion1(lista1)
print(lista3)

def insertion_sort(data):    #EJEMPLO DE FAUSTO
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
