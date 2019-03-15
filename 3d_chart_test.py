import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
from math import fmod

def multiplication(x, y):
  return x * y

def addition(x, y):
  return x + y

def palindrome_multiplication(x, y):
  product = x * y

  return product if is_palindrome(product) else 0


def print_array(array, name):
  print('')
  print(name)
  print('ndim', array.ndim)
  print('shape', array.shape)
  print('size', array.size)
  print(array)
  print('ravel', np.ravel(array))

def plot3d(x, y, func):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection = '3d')

  X, Y = np.meshgrid(x, y)

  zs = np.array([func(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
  Z = zs.reshape(X.shape)

  ax.scatter(X, Y, Z)

  ax.set_xlabel('X Label')
  ax.set_ylabel('Y Label')
  ax.set_zlabel('Z Label')

  plt.show()

def calculate_primes(number_of_primes):
  primes = [2, 3]
  number = 3

  while number_of_primes > len(primes):
    number += 2

    if is_prime_in_range(number, primes):
      primes.append(number)

  return np.array(primes)


def is_prime_in_range(number, primes):
  for prime in primes:
    if fmod(number, prime) == 0:
      return False

  return True

def is_palindrome(number):
  original = number
  reverse = 0

  while number != 0:
    digit = number % 10
    number = int(number / 10)
    reverse = reverse * 10 + digit

  return original == reverse

x1 = x2 = calculate_primes(50)

plot3d(x1, x2, palindrome_multiplication)













# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')


# x = np.arange(0, 50, 1)
# y = np.arange(0, 50, 1)

# print(x)
# print(y)

# X, Y = np.meshgrid(x, y)

# print(np.ravel(X))

# print_array(X, 'X')
# print_array(Y, 'Y')

# zs = np.array([fun(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
# Z = zs.reshape(X.shape)

# print_array(zs, 'zs')
# print_array(Z, 'Z')


# ax.plot_surface(X, Y, Z)

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()















# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import pyplot
# import numpy

# def y_func(x1, x2):
#   return x1 * x2

# max_value = 100

# X1 = numpy.array([])
# X2 = numpy.array([])
# Y  = numpy.array([])

# for x1 in range(max_value):
#   for x2 in range(max_value):
#     numpy.append(X1, [x1])
#     numpy.append(X2, [x2])
#     numpy.append(Y, [y_func(x1, x2)])

# figure = pyplot.figure()

# axis1 = figure.add_subplot(111, projection = '3d')
# axis1.plot_wireframe(X1, X2, numpy.array([Y, X1]))

# axis1.set_xlabel('x1 axis')
# axis1.set_ylabel('x2 axis')
# axis1.set_zlabel('y axis')

# pyplot.show()


# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np

# max_value = 100

# X1 = []
# X2 = []
# Y1 = []
# Y2 = []

# def y_func_1(x1, x2):
#   return x1 * x2

# def y_func_2(x1, x2):
#   return 0

# for x1 in range(max_value):
#   for x2 in range(max_value):
#     X1.append(x1)
#     X2.append(x2)
#     Y1.append(y_func_1(x1, x2))
#     Y2.append(y_func_2(x1, x2))

# X1 = np.array(X1)
# X2 = np.array(X2)
# Y1 = np.array(Y1)
# Y2 = np.array(Y2)

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# # Plot the surface.
# surf = ax.plot_surface(X1, X2, np.array([Y1, Y2]), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)

# # Customize the z axis.
# # ax.set_zlim(-1.01, 1.01)
# # ax.zaxis.set_major_locator(LinearLocator(10))
# # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()
