# Code by Viswaksena-35
import numpy as np
import matplotlib.pyplot as plt

g = 9.81 
v0 = 28
y0 = 0
angles = np.arange(15, 75 + 15, 15) 
distances = np.arange(0, 80 + 5, 5) 

theta = np.deg2rad(angles)

results = np.zeros((len(distances), len(angles)))

for i in range(len(angles)):
    for j in range(len(distances)):
        x = distances[j]
        results[j, i] = y0 + x * np.tan(theta[i]) - (g * x**2) / (2 * v0**2 * np.cos(theta[i])**2)

plt.figure()
plt.plot(distances, results, linewidth=2)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Trajectories')
plt.legend([f'Angle = {angle}°' for angle in angles], loc='best')
plt.axis([0, 80, 0, np.max(results)])
plt.show()
