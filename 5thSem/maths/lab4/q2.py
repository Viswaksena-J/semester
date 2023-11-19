# Code by Viswaksena-35
import numpy as np
import matplotlib.pyplot as plt

density_append = []
z_append = []
for z in range(-5,5):
    density_function = (1/np.sqrt(2*np.pi))*np.exp((-z**2)/2)
    density_append.append(density_function)
    z_append.append(z)
    print("z=",z,"density=",density_function)
plt.plot(z_append,density_append)
plt.xlabel('z')
plt.ylabel('Frequency')
plt.show()
