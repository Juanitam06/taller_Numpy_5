#Numpy: Biblioteca para realizar calculos numericos en arreglos n-dimesnioanles

import numpy as np

#crear ndarray 2 dimensiones a partir de una lista

A = np.array([[1,5], [7,9]])
B = np.array([[2,0], [1,3]])

#Producto punto entre ndarrays

C= np.dot(A,B)
print(C)

#Solucion de un sistema de ecuaciones con Numpy
m_solucion =np.array([5,17])
m=np.linalg.solve(A,m_solucion)
print(m)