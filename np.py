import numpy as np

# NumPy is a package for scientific computing in Python
# Provides multidimensional array object, various derived objects
# such as marked arrays and matrices
# Core of the package is the ndarray object

# NumPy arrays have a fixed size at creation, unlike Python lists
# (which can grow dynamically). Changing the size of an ndarray will # create a new array and delete the original.

# The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements


# Consider taking dot product in Python
# c = []
# for i in range(len(a)):
#     c.append(a[i]*b[i])

# DRAWBACK: This is slow if each list contains millions of elements
# Same code above can be done in C to avoid Python overhead of interpreting Python code and manipulating Python objects, but avoids the simplicity of coding in Python
# Hence, we use

###############################################################################
# ndarray

# ndarray is NumPy's array class, known as alias array

# ndarray.ndim - no. of axes (dimensions) of array
# ndarray.shape - dimensions of array; n rows and m columns gives (n,m)
#                 length of shape tuple is number of axes, ndim
# ndarray.size - total number of elements in the array; also n*m from shape
# ndarray.dtype - object describing type of elements in array
# ndarray.itemsize - size in bytes of each element in array
#                    float64 has itemsize 8 and complex32 has itemsize 4
# ndarray.data - buffer containing actual elements of array
#                normally don't use this attribute b/c want to access indices


# Creates range 0-14 (inclusive), then makes it a 3x5 matrix
a = np.arange(15).reshape(3, 5)
print(a)
# a gives object ndarray

### Creating Arrays

# use array function
a = np.array([2,3,4])
b = np.array([1.2, 3.5, 5.1])
print(a.dtype) # int64
print(b.dtype) # float64

# NOTE: Must feed array function with list input

# this creates 2D array
b = np.array([(1.5,2,3), (4,5,6)])

# array([[ 1.5,  2. ,  3. ],
#       [ 4. ,  5. ,  6. ]])

# can also specify data type at creation time
c = np.array( [ [1,2], [3,4] ], dtype=complex )

# creates 3x4 array of zeros
np.zeros( (3,4) )

# creates 2x3x4 array of ones
np.ones( (2,3,4), dtype=np.int16 )

# uninitialized 2x3 array with random values based on computer memory size
np.empty( (2,3) )

# arange function returns arrays instead of lists from python's range function
# go from 10-30, increment by 5
np.arange( 10, 30, 5 ) # array([10, 15, 20, 25])

np.linspace( 0, 2, 9 ) # 9 numbers from 0 to 2

# NumPy operations
a = np.array( [20,30,40,50] )
b = np.arange( 4 ) # array([0, 1, 2, 3])
c = a-b # array([20, 29, 38, 47])
b**2 # array([0, 1, 4, 9])
10*np.sin(a) # array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
a<35 # array([ True, True, False, False])

# Given A and B as matrices
# A*B - elementwise product --- e.g. C[r][c] = A[r][c]*B[r][c]
# A@B - matrix product --- regular matrix mulitplication
# A.dot(B) - matrix product