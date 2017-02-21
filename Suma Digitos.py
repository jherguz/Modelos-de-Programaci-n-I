# -*- coding: utf-8 -*-
def sumaDigitos(numero):
    if numero==0:
        return 0
    elif numero!=0:
        return sumaDigitos(numero/10)+(numero%10)
numero=int(raw_input("Digite el numero "))
print sumaDigitos(numero)