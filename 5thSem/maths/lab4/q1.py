# Code by Viswaksena-35
import numpy as np
import matplotlib.pyplot as plt
q0 = 10
R = 60
L = 9
C = 0.00005
t_append = []
charge1 = []
for t in np.arange(0, 0.9, 0.01):
    charge = q0 * np.exp(-(R * t) / (2 * L)) * np.cos(np.sqrt((1 / (L * C)) - (R / (2 * L))**2) * t)
    t_append.append(t)
    charge1.append(charge)
    print("t=",t,"charge=",charge)
plt.plot(t_append, charge1)
plt.show()
