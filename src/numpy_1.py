import numpy as np

# Print numpy version
print(f'Numpy Version: {np.__version__}')

numpy_array_1 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"NumPY Array 1:{numpy_array_1}")
print(f"NumPY Array 1 Dimension:{numpy_array_1.ndim}")


# 0D array
a_0d = np.arange(42)
print(f"0D Array:{a_0d}")


# 1D array
a_1d = np.arange(3)
print(f"1D Array:{a_1d}")

# 2D array
a_2d = np.arange(12).reshape((3, 4))
print(f"2D Array:{a_2d}")

# 3D array
a_3d = np.arange(24).reshape((2, 3, 4))
print(f"3D Array:{a_3d}")

# Number of dimensions of numpy.ndarray: ndim
# The number of dimensions of numpy.ndarray can be obtained as an integer value int with attribute ndim.

print(a_1d.ndim)
# 1

print(type(a_1d.ndim))
# <class 'int'>

print(a_2d.ndim)
# 2

print(a_3d.ndim)
# 3

# Shape of numpy.ndarray: shape The shape (= length of each dimension) of numpy.ndarray can be obtained as a tuple
# with attribute shape. Even in the case of a one-dimensional array, it is a tuple with one element instead of an
# integer value. Note that a tuple with one element has a trailing comma.
# One-element tuples require a comma in Python

print(a_1d.shape)
# (3,)

print(type(a_1d.shape))
# <class 'tuple'>

print(a_2d.shape)
# (3, 4)

print(a_3d.shape)
# (2, 3, 4)

# For example, in the case of a two-dimensional array, it will be (number of rows, number of columns). If you only
# want to get either the number of rows or the number of columns, you can get each element of the tuple.

row_shape = a_2d.shape[0]
print(f"Shape of the row:{row_shape}")

column_shape = a_2d.shape[1]
print(f"Shape of the column:{column_shape}")

# Size of numpy.ndarray (total number of elements): size
# The size (= total number of elements) of numpy.ndarray can be obtained with the attributesize

print(a_1d.size)
# 3

print(type(a_1d.size))
# <class 'int'>

print(a_2d.size)
# 12

print(a_3d.size)
# 24

# Size of the first dimension of numpy.ndarray: len() len() is the built-in function that returns the number of
# elements in a list or the number of characters in a string. For numpy.ndarray, len() returns the size of the first
# dimension. Equivalent to shape[0] and also equal to size only for one-dimensional arrays.

print(len(a_1d))
# 3

print(a_1d.shape[0])
# 3

print(a_1d.size)
# 3

print(len(a_2d))
# 3

print(a_2d.shape[0])
# 3

print(len(a_3d))
# 2

print(a_3d.shape[0])
# 2



