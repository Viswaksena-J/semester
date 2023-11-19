# Code by Viswaksena-35
import numpy as np
import matplotlib.pyplot as plt

def butterfly_curve(theta):
    r = np.exp(np.sin(theta)) - 2 * np.cos(4 * theta) - np.sin((2 * theta - np.pi) / 24) ** 5
    return r

theta_values = np.arange(0, 8 * np.pi, np.pi / 32)

r_values = butterfly_curve(theta_values)

plt.polar(theta_values, r_values, 'r--',color='blue')
plt.title('Butterfly Curve')
plt.show()
