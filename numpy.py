import numpy as np

# NumPy is a package for scientific computing in Python
# Provides multidimensional array object, various derived objects
# such as marked arrays and matrices
# Core of the package is the ndarray object

# NumPy arrays have a fixed size at creation, unlike Python lists
# (which can grow dynamically). Changing the size of an ndarray will # create a new array and delete the original.

# The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements


# Consider taking dot product in Python
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])

# DRAWBACK: This is slow if each list contains millions of elements
# Same code above can be done in C to avoid Python overhead of interpreting Python code and manipulating Python objects, but avoids the simplicity of coding in Python
# Hence, we use