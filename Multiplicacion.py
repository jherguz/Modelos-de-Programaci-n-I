# -*- coding: utf-8 -*-
def multiplicacion(a,b):
    if b==0:
        return 0
    elif b!=0:
        return a+multiplicacion(a,b-1)
a=int(raw_input("Digite un numero "))
b=int(raw_input("Digite un numero "))
print multiplicacion(a,b)