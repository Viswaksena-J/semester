# Code by Viswaksena-35
import numpy as np
import matplotlib.pyplot as plt

n = [0.035,0.020,0.015,0.030,0.022]
S = [0.0001,0.0002,0.0010,0.0007,0.0003]
B = [10,8,20,24,15]
H = [2,1,1.5,3,2.5]

Manning_equation_append = []
matrix = np.matrix([n,S,B,H])
i_append = []
for i  in range(4):
    Manning_equation = (np.sqrt(S[i])/n[i])*(((B[i]*H[i])/(B[i]+2*H[i]))**2/3)
    Manning_equation_append.append(Manning_equation)
    i_append.append(i)
    print("i=",i,"Manning_equation=",Manning_equation)

plt.plot(i_append,Manning_equation_append)
plt.show()