import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

def lorenz_system(t, state):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Initial conditions and time span
initial_state = np.random(3)
t_span = (0, 50)
t_eval = np.linspace(0, 50, 10000)

# Solve the differential equations
solution = solve_ivp(lorenz_system, t_span, initial_state, t_eval=t_eval)

# Extract solutions
x, y, z = solution.y

# Create 3D plot
fig = plt.figure(figsize=(8, 6))


# 2D projections
ax1 = fig.add_subplot(211)
ax1.plot(x, y, 'r-', alpha=0.7, linewidth=0.5)
ax1.set_xlabel(r'$x$', fontsize=12)
ax1.set_ylabel(r'$y$', fontsize=12)
ax1.set_title(r'$x-y$ Projection', fontsize=12)

ax2 = fig.add_subplot(212)
ax2.plot(t_eval, x, 'r-', alpha=0.7, linewidth=0.5)
ax2.plot(t_eval, y, 'b-', alpha=0.7, linewidth=0.5)
ax2.plot(t_eval, z, 'g-', alpha=0.7, linewidth=0.5)
ax2.set_xlabel(r'$t$', fontsize=12)
ax2.set_ylabel(r'$x,y,z$', fontsize=12)
ax2.set_title(r'time series', fontsize=12)

plt.tight_layout()
plt.show()
