# -*- coding: utf-8 -*-
def potenciacion(n,m):
    if m == 0:
        return 1
    elif m!=0:
        return n*potenciacion(n,m-1)
base=int(raw_input("Digite la base "))
exponente=int(raw_input("Digite el exponente "))
print potenciacion(base,exponente)