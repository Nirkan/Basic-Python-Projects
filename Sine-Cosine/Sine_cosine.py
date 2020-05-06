# import packages

import numpy as np

x = np.linspace(0, 2*np.pi, 100)
ys = np.sin(x)
yc = np.cos(x)

import matplotlib.pyplot as plt
plt.style.use('dark_background')

plt.plot(x, ys, color = 'blue', linestyle = 'dashed')
plt.plot(x, yc, color = 'orange', linestyle = 'dashed')
plt.xlabel('x', fontsize = 11, fontweight = 'bold')
plt.ylabel('y', fontsize = 11, fontweight = 'bold')
plt.title('Functions')
plt.grid(True)
plt.show()
