# -*- coding: utf-8 -*-
def fibonacci(n):
    if n==1 or n==2:
        return 1
    elif n>2:
        return(fibonacci(n-1)+fibonacci(n-2))
numero = int(raw_input("Digite numero: "))
print fibonacci(numero)