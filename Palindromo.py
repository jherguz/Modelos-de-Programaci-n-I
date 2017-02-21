# -*- coding: utf-8 -*-
def palindromo(palabra):
    if len(palabra)<2:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return palindromo(palabra[1:-1])
palabra=raw_input("Digite la frase ")
print palindromo(palabra)