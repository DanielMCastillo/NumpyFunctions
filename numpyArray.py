import numpy as np

matriz = np.array([1,2,3,4,5])
print(matriz)


lista = [1,3,5]
lista.append(7)
print(lista)

matriz = np.array([2,4,6])
matriz = np.append(matriz, 8)
print(matriz)

# Sumar valor a matriz
matriz = matriz + np.array([5])
print(matriz)

#operaciones aritmeticas
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b) # Suma
print(a - b) # Resta
print(a * b) # Multiplicacion
print(a / b) # Division
print(a ** b) # Potenciacion
print(a % b) # Modulo
print(a // b) # Division entera