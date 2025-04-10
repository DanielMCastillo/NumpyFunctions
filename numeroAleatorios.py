# numpy aleatorios
import numpy as np
m = np.random.randint(10)
print(m)

# aleatorio a una dimension
m1 = np.random.randint(10,size=5)
print(m1)

# aleatorio a dos dimensiones
m2 = np.random.randint(10,size=(3,4))
print(m2)

#aletorios precisos
a = np.random.rand(3,4) #aleatorio entre 0 y 1
print(a)

#sacar algun aleatorio de un array
m3 = np.random.choice([1,2,3,4,5],2) #saca 2 aleatorios de m1
print(m3)

#distribucion aleatorio de matriz
m4 = np.random.normal(0,1,(3,4)) #distribucion normal
print(m4)
