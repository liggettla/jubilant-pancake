# numPy uses C to compute things and then passes to python
# this makes numPy very fast

import numpy as np

def test_run():
    # convert list to 1D array
    np.array([2, 3, 4])
    np.array([(2,3,4), (5,6,7)])

# empty arrays actually initialize with random values dependent on current memory state
    # 1D array
    np.empty(5)
    # 2D array
    np.empty((5,4))
    # 3D array
    np.empty((5,4,3))
    # 2D array with all values equal to 1
    np.ones((5,4), dtype='i')
    # default values are float, using dtype to change
    np.array([1, 2, 3], dtype='i')
    # generate random number array sampled from [0.0, 1.0]
    np.random.random((5,4)) # pass in a tuple
    np.random.rand(5,4) # not a tuple
    # sample numbers from a gaussian distribution with mean=0 SD1=1
    x = np.random.normal(loc=0, scale=1, size=(2,3))
    np.random.normal
    np.mean(x)
    np.std(x)
    # generate random integers
    np.random.randint(10) # single integer between 0-10
    np.random.randint(0, 10) # same as above
    np.random.randint(0, 10, size=5) # integers between 0-10 filling 1D array
    np.random.randint(0, 10, size=(2, 4)) # 2x3 array of 0-10 integers

# reshaping arrays
a = np.random.random((5, 4)) # 5x4 array of random numbers
a
a.shape # displays array dimensions
a.shape[0] # displays number of rows
a.shape[1] # displays number of columns
len(a.shape) # displays number of dimensions
a.size # number of elements in array
a.dtype # shows type


if __name__ == "__main__":
    test_run()
