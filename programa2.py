import numpy as np
#matplotlib tiene muchos modulos. Importar uno solo
import matplotlib.pyplot as plt

#dibujar una funcion seno
#crear un ndarray de 1 dimension, 100 elementos equiespaciados
#de 0 a 2*pi

x= np.linspace(0,2*np.pi, 100)
y= np.sin(x)

#usar matplotlib
#definir el tamaño de la figura

plt.figure(figsize=(8,4))
plt.title("Mi primer grafico cientifico en  Programacion")
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Seno de x")
plt.grid(True)
plt.show()
