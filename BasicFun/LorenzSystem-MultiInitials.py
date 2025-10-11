import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

def lorenz_system(t, state, sigma=10, rho=28, beta=8/3):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Multiple initial conditions
initial_conditions = [
    [1.0, 1.0, 1.0],
    [0.1, 0.1, 0.1],
    [-1.0, -1.0, -1.0],
    [10.0, 10.0, 10.0]
]

colors = ['red', 'blue', 'green', 'orange']
t_eval = np.linspace(0, 30, 5000)

# Create plot
fig = plt.figure(figsize=(15, 5))

# 3D plot
ax1 = fig.add_subplot(131, projection='3d')

for i, (init, color) in enumerate(zip(initial_conditions, colors)):
    solution = solve_ivp(lorenz_system, (0, 30), init, t_eval=t_eval)
    x, y, z = solution.y
    ax1.plot(x, y, z, color=color, alpha=0.7, linewidth=0.8, 
             label=f'Init {i+1}')

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Lorenz Attractor - Multiple Trajectories')
ax1.legend()

# Time series
ax2 = fig.add_subplot(132)
solution = solve_ivp(lorenz_system, (0, 30), initial_conditions[0], t_eval=t_eval)
x, y, z = solution.y
ax2.plot(t_eval, x, 'r-', label='X', alpha=0.7)
ax2.plot(t_eval, y, 'g-', label='Y', alpha=0.7)
ax2.plot(t_eval, z, 'b-', label='Z', alpha=0.7)
ax2.set_xlabel('Time')
ax2.set_ylabel('Value')
ax2.set_title('Time Series')
ax2.legend()

# Phase portrait (X-Z)
ax3 = fig.add_subplot(133)
for i, (init, color) in enumerate(zip(initial_conditions, colors)):
    solution = solve_ivp(lorenz_system, (0, 30), init, t_eval=t_eval)
    x, y, z = solution.y
    ax3.plot(x, z, color=color, alpha=0.7, linewidth=0.8, 
             label=f'Init {i+1}')

ax3.set_xlabel('X')
ax3.set_ylabel('Z')
ax3.set_title('X-Z Phase Portrait')
ax3.legend()

plt.tight_layout()
plt.show()
