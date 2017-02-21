# -*- coding: utf-8 -*-

def invertir(a,inferior,superior):
    while(inferior<=superior):
        aux=a[superior]
        a[superior]=a[inferior]
        a[inferior]=aux
        return invertir(a,inferior+1,superior-1)
    return a

lista =[]

elemento= raw_input("Digite elemento: ")

while elemento!="":
    lista.append(elemento)
    elemento = raw_input("Siguiente elemento: ")

print lista
print invertir(lista,0,len(lista)-1)