#Code by Viswaksena J/35

mass = 68.1#kg
cd = 0.25#lumped drag coefficient
g = 9.81

print("\033[3;32;40m" + "Example 1.1" + "\033[m")

import numpy as np
import matplotlib.pyplot as plt

t_values = []
y_values = []

for t in range(0, 16, 2):
    y = np.sqrt(g*mass/cd) * np.tanh(np.sqrt(g*cd/mass) * t)
    t_values.append(t)
    y_values.append(y)
    print("t =", t, "y =", y)


plt.plot(t_values, y_values, 'ro-')
plt.xlabel('t,s')
plt.ylabel('v,m/s')
plt.title('Line Plot for Different t Values(Analytical Solution)')
plt.grid(True)
plt.legend()
plt.show()

print("------------------------------------")

print("\033[3;32;40m" + "Example 1.2" + "\033[m")
#Eulers method
# V = U + at
#v(ti+1)=v(ti)+ g−cdv(ti)2 (ti+1−ti) m
# New value = old value + slope × step size

velocity = 0
t0 = 0

t_values2 = []
y_values2 = []

for t in range(0, 16, 2):
    velocity = velocity + (g-(cd/mass)*(velocity**2)) * (t-t0)
    t_values2.append(t)
    y_values2.append(velocity)    
    print(t, velocity)
    velocity = velocity
    t0 = t

plt.figure(figsize=(8, 6))
plt.plot(t_values, y_values, 'ro-', label='Analytical Solution')
plt.plot(t_values2, y_values2, 'bo-', label='Numerical Solution')
plt.xlabel('t,s')
plt.ylabel('v,m/s')
plt.title('Comparison of the numerical and analytical solutions for the bungee jumper problem')
plt.grid(True)
plt.legend()

plt.show()

    
