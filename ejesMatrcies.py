#ejes en matrices
import numpy as np

#suma numerica con el eje en 0
a = np.array([[1,2,3],[4,5,6]])
print(a.sum(axis=0)) #suma por columnas
print(a.sum(axis=1)) #suma por filas
print(" ")
##dos matricces
m1 = np.array([[1,3],[4,5]])
m2 = np.array([[7,9],[10,11]])
print(m1)
print(" ")
print(m2)
print(" ")
print(np.concatenate([m1,m2], axis=1)) #suma de matrices