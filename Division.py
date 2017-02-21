# -*- coding: utf-8 -*-
def division(a,b):
    if a<b:
        return 0
    elif a>=b:
        return division(a-b,b)+1
a=int(raw_input("Digite el dividendo "))
b=int(raw_input("Digite el divisor "))
print division(a,b)