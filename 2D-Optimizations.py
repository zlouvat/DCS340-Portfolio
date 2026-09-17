import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

# Toy Function # # # # # # # # # # # #
# f(x,y) = (x-2)**2 - xy + (y-3)**2
#  # # # # # # # # # # # # # # # # # #
def vizualization():
    def f(coords):
        x, y = coords
        output = (x-2)**2 - x*y + (y-3)**2
        return output

    # Visualizing f(x)

    x_range = np.linspace(-5, 5, 100)
    y_range = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = f((X, Y))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X,Y,Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    plt.show()