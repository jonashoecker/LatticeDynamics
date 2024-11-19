import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.interpolate import interp1d

A = 1
x_original = [1, 2, 3, 4, 5, 6, 7, 8]

fig, axes = plt.subplots(2, 4, figsize=(12, 8))
axes = axes.flatten()

for N in range(1, 9):
    y_original = [A * m.sin(j * N * m.pi / 9) for j in x_original]
    
    interp_func = interp1d(x_original, y_original, kind='cubic')
    
    x_smooth = np.linspace(min(x_original), max(x_original), 100)
    y_smooth = interp_func(x_smooth)
    
    ax = axes[N-1]
    
    ax.plot(x_smooth, y_smooth, label=f'Smooth Curve N={N}')
    
    ax.scatter(x_original, y_original, color='red', zorder=5, label='Original Points')
    
    ax.set_title(f'Plot for N={N}')
    ax.legend(loc='upper right', fontsize=8)

plt.tight_layout()
plt.show()
