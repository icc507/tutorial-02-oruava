# -*- coding: utf-8 -*-
"""problema1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RDCNDQK6B7RKB1JGooGgnd120rPxRcSs
"""

#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t = tuple(input().split())
m = tuple(input().split())
t3 = m+t+m

tuplafinal = tuple()
for palabra in t3:
    try:
        numero = int(palabra)
        tuplafinal += (numero,)
    except ValueError:
        tuplafinal += (palabra,)

print(tuplafinal)