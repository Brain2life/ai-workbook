import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare grid
x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
X1, X2 = np.meshgrid(x1, x2)

# Define functions
Z_linear     = 3*X1 + 2*X2
Z_squared    = 3*X1**2 + 2*X2
Z_sine       = 3*X1 + 2*np.sin(X2)

# Plotting
fig = plt.figure(figsize=(18, 5))

# Plot 1: Linear
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X1, X2, Z_linear, cmap='viridis')
ax1.set_title("Linear: 3x₁ + 2x₂")
ax1.set_xlabel("x₁")
ax1.set_ylabel("x₂")
ax1.set_zlabel("z")

# Plot 2: Squared
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X1, X2, Z_squared, cmap='plasma')
ax2.set_title("Nonlinear: 3x₁² + 2x₂")
ax2.set_xlabel("x₁")
ax2.set_ylabel("x₂")
ax2.set_zlabel("z")

# Plot 3: Sine
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X1, X2, Z_sine, cmap='coolwarm')
ax3.set_title("Nonlinear: 3x₁ + 2sin(x₂)")
ax3.set_xlabel("x₁")
ax3.set_ylabel("x₂")
ax3.set_zlabel("z")

# Save the plot before showing it
plt.tight_layout()
plt.savefig("gauss_visualization.png", dpi=300)
plt.show()
