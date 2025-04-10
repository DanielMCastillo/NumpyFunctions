#algebra lineal
import numpy as np
#Funciones para calcular algebra lineal
#Suma, resta, multiplicacion y division de matrices
#Multiplicacion de matrices
m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.array([[7,8,9],[10,11,12]])
#Multiplicacion de matrices
multiplicacion = np.dot(m1,m2)
print("La multiplicacion de matrices es: ")
print(multiplicacion)
#Multiplicacion de matrices por un escalar
m1 = np.array([[1,2,3],[4,5,6]])
m2 = 2
multiplicacion = m1 * m2
#Multiplicacion de matrices por una matriz inversa
m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.linalg.inv(m1)
multiplicacion = np.dot(m1,m2)
#Multiplicacion de matrices por una matriz identidad
m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.eye(3)
multiplicacion = np.dot(m1,m2)
#Multiplicacion de matrices por una matriz diagonal
m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.diag([1,2,3])
multiplicacion = np.dot(m1,m2)
#Multiplicacion de matrices por una matriz transpuesta
m = np.array([[1,2,3],[4,5,6]])
print("La matriz es: ")
print(m)
print("")
m1 = np.array([[1],[2],[3]])
print(m1)
#transpuesta de matrtiz
print(np.transpose(m1))
mt = m * np.transpose(m1)