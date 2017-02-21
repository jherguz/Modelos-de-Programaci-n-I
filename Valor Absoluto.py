# -*- coding: utf-8 -*-
def valorAbsoluto(numero):
    if numero>=0:
        return numero
    elif numero<0:
        return valorAbsoluto(numero*(-1))
numero = int(raw_input("Digite un numero "))
print valorAbsoluto(numero)