import numpy as np
m2d = np.array([[1,2,3],[4,5,6]])
print(m2d)

#Listas con arrays
lista = [1,2,3,4,5]
matriz = np.array(lista)
print(matriz)


lista = [[1,2,3],[4,5,6]]
matriz = np.array(lista)
print(matriz)

#matriz bidimensional
#funcion arange para crear un array de 1 a 10
#funcion reshape para cambiar la forma del array
#reshape(2,5) cambia la forma del array a 2 filas y 5 columnas
m = np.arange(1,11).reshape(2,5)
print(m)
