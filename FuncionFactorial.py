# -*- coding: utf-8 -*-
"""
author: Alejandra Jiménez Soto
date: 10/21/2022

"""

def factorialIterativo(n):
    print("Ingresando al factorial iterativo")
    temporal = 1
    for i in range(1,n+1):
        temporal= temporal*i
    return (temporal)

def factorialRecursivo(n):
    print("Ingresando al factorial recursivo")
    if(n==0):
        return(1)
    else:
        return n*factorialRecursivo(n-1)
    
print(factorialIterativo(5))
print(factorialRecursivo(5))