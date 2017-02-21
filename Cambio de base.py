# -*- coding: utf-8 -*-
def decimalaBinario(numero):
    if numero<2:
        print numero,
    elif numero >=2:
        decimalaBinario(numero/2)
        print numero%2,
numero = int(raw_input("Digite un numero para pasar de decimal a binario"))
decimalaBinario(numero)