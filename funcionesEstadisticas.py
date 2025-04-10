#estadistica
#Funciones para calcular estadisticas
#Media, mediana, moda, varianza y desviacion estandar
import numpy as np  
m = np.array([1,2,3,4,5,6,7,8,9,10])
print(m)
print("La media es: ", np.mean(m))
print("La mediana es: ", np.median(m))
print("La moda es: ", np.argmax(np.bincount(m))) #moda
print("La varianza es: ", np.var(m))
print("La desviacion estandar es: ", np.std(m))
#valor maximo
print("El valor maximo es: ", np.max(m))
#valor minimo
print("El valor minimo es: ", np.min(m))
#rango
print("El rango es: ", np.max(m)-np.min(m))
#cuartiles
print("El primer cuartil es: ", np.percentile(m, 25))
print("El segundo cuartil es: ", np.percentile(m, 50))
print("El tercer cuartil es: ", np.percentile(m, 75))
#desviacion estandar poblacional
print("La desviacion estandar poblacional es: ", np.std(m, ddof=0))
#desviacion estandar muestral
print("La desviacion estandar muestral es: ", np.std(m, ddof=1))
