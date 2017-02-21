# -*- coding: utf-8 -*-

def menor(a,ini,fin):
    if ini==fin:
        return a[fin]
    if a[ini]>a[fin]:
        return menor(a,ini+1,fin)
    else:
        return menor(a,ini,fin-1)

listas=[]
lista =[]
i=0
auxiliar=1
while auxiliar!=-0:
    elemento= int(raw_input("Digite elemento: "))
    while elemento!=-0:
        lista.append(elemento)
        elemento = int(raw_input("Siguiente elemento: "))
    listas.append(menor(lista,0,len(lista)-1))
    print lista
    for x in lista[:]:
        lista.remove(x)
    auxiliar= int(raw_input("Siguiente lista? "))

print listas