m = 68.1#kg
cd = 0.25#lumped drag coefficient
g = 9.81

import numpy as np
velocity = np.sqrt(g*m/cd) * np.tanh(np.sqrt(g*cd/m) * 12)
print(velocity)

for t in range(0, 16, 2):
    print(t, np.sqrt(g*m/cd) * np.tanh(np.sqrt(g*cd/m) * t))

#Eulers method
# V = U + at
#v(ti+1)=v(ti)+ g−cdv(ti)2 (ti+1−ti) m
# New value = old value + slope × step size
import matplotlib.pyplot as plt
velocity = 0
t0 = 0
for t in range(0, 16, 2):
    velocity = velocity + (g-(cd/m)*(velocity**2)) * (t-t0)    
    print(t, velocity)
    velocity = velocity
    t0 = t
plt.plot(t, velocity, 'ro')
    
