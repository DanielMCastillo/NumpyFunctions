#operaciones con matrices
import numpy as np 
m = np.arange(24).reshape(4,6)
print(m[3,4])
print(m)

#ejemplo -  ordenar array
m1 = np.array([1,2,7,5,6])
print(np.sort(m1))

#ejemplo - potencias en matrices
m1 = np.array([1,2])
print(np.array(m1**2)) #potencia de 2

#condicion
m2 = np.array([1,2,3,4])
print(np.array(m2>2)) #imprime los elementos mayores a 2


#ejemplo valor mayor de un array
m3 = np.array([1,2,3,4])
print(np.max(m3)) #imprime el valor mayor del array

#combinar matrices
matrizm1 = np.array([1,2,3,4,5])
matriz2 = np.array([6,7,8,9,10])
print(np.concatenate((matrizm1,matriz2))) #concatena las matrices

## matriz bidimenciona
md1 = np.array([[1,2],[3,4]])
md2 = np.array([[5,6],[7,8]])
print(np.concatenate((md1,md2))) #concatena las matrices
#suma de matrices
print(np.add(md1,md2)) #suma de matrices
#resta de matrices
print(np.subtract(md1,md2)) #resta de matrices
#multiplicacion de matrices
print(np.multiply(md1,md2)) #multiplicacion de matrices
#division de matrices
print(np.divide(md1,md2)) #division de matrices
#potencia de matrices
print(np.power(md1,md2)) #potencia de matrices


#funcion dot 
print(md1.dot(md2)) 
