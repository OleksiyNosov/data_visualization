from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

max_value = 100

X1 = []
X2 = []
Y1 = []
Y2 = []

def y_func_1(x1, x2):
  return x1 * x2

def y_func_2(x1, x2):
  return 0

for x1 in range(max_value):
  for x2 in range(max_value):
    X1.append(x1)
    X2.append(x2)
    Y1.append(y_func_1(x1, x2))
    Y2.append(y_func_2(x1, x2))

X1 = np.array(X1)
X2 = np.array(X2)
Y1 = np.array(Y1)
Y2 = np.array(Y2)

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(X1, X2, np.array([Y1, Y2]), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
