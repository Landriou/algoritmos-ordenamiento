from linkedlist import *
from algo1 import *
def SelectionSort(L):
    Ordenarlista(L,0)

def Ordenarlista(L,n):
    currentnode = L.head
    mayor = 0
    if n == length(L)-1 : #Caso base de la recursividad
        return True
    for i in range(length(L)-n):
        if currentnode.value > mayor: #Si encuentro el mayor me lo guardo
            mayor = currentnode.value
        currentnode = currentnode.nextNode
    move(L,search(L, mayor),length(L)-1-n) #Busco el mayor e intercambio posiciones mandandolo al final
    Ordenarlista(L, n+1)

def BubbleSort(L):
    currentnode = L.head
    largo = length(L)
    ordenados = 0
    for i in range(largo):
        for n in range(largo - 1 - ordenados):
            if currentnode.value > currentnode.nextNode.value:
                #Voy comparando uno con el siguiente si el anterior es mayor los intercambio
                move(L,n,n+1)
            else:
                currentnode = currentnode.nextNode
        ordenados = ordenados + 1 #Para que no llegue a las ultimas posiciones que ya se ordenaron se va restando
        currentnode = accesposition(L,0)

def InsertionSort(L):
    L2 = LinkedList()
    currentnode = L.head
    largo = length(L)
    A = Array(largo,0)
    for n in range(largo):#Transformo la lista en array
        A[n] = currentnode.value
        currentnode = currentnode.nextNode
    for i in range(largo):
        actual = A[i] #Me guardo el actual
        j = i
        while j > 0 and A[j-1] >actual: #Busco el elemento 
            A[j] = A[j-1]
            j = j -1
        A[j] = actual #Y lo reemplazo
    for k in range(largo):
        add(L2,A[k])
    L2 = inverse(L2) #Lo vuelvo a pasar a lista
    L.head = L2.head

L = LinkedList()
add(L,5)
add(L,5)
add(L,7)
add(L,9)
add(L,0)
add(L,1)
add(L,8)
add(L,2)
imprimirlista(L)
SelectionSort(L)
print("")
imprimirlista(L)

L2 = LinkedList()
add(L2,5)
add(L2,5)
add(L2,7)
add(L2,9)
add(L2,0)
add(L2,1)
add(L2,8)
add(L2,2)
BubbleSort(L2)

imprimirlista(L2)
L3 = LinkedList()
add(L3,5)
add(L3,5)
add(L3,7)
add(L3,9)
add(L3,0)
add(L3,1)
add(L3,8)
add(L3,2)
InsertionSort(L3)
print("")
imprimirlista(L3)