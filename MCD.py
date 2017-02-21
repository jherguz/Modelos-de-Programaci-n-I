# -*- coding: utf-8 -*-
def mcd(a,b):
    if b==0:
        return a
    return mcd(b,a%b)

a=int(raw_input("Digite el primer numero "))
b=int(raw_input("Digite el segundo numero "))

print mcd(a,b)