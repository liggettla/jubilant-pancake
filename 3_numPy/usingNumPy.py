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

    # operations on ndarrays
    np.random.seed(693) # seed the random number generator
    np.random.randint(1000000) # now always gives the same number
    a = np.random.randint(0, 10, size=(5, 4)) # 5x4 random int in 0-10
    #print "Array:\n", a
    #print "Sum of all elements:", a.sum() # sums all array elements

    # iterate over rows to compute sum of each column
    a.sum(axis=0)
    # iterate over rows to compute sum of each row
    a.sum(axis=1)
    # min/max/mean
    a.min(axis=0) # min of each column
    a.max(axis=1) # max of each row
    a.mean() # mean of all elements

    # searching for the index of elements
    # http://docs.scipy.org/doc/numpy/reference/routines.sort.html
    a
    np.argmax(a) # only prints first instance of max val

# accessing arrary elements
    a
    element = a[3, 2] # [row, column]
    element

# using slicing
    a[0, 1:3] # row zero columns 1-2
    a[0:2, 0:2] # rows 0-1 columns 0-1
    a[:, 0:3:2] # every row, columns 0-3 not including 3 in steps of 2

# assigning values to specific array locations
    a[0, 0] = 1 # change the 0, 0 value to 1
    a[0,:] = 2 # assign the entire first row a value of 2
    a[:, 3] = [1, 2, 3, 4, 5] # assign list values to the 4th column
    a

# indexing an array with another array
# basically just allows multiple positions to be accessed at once
    indices = np.array([1,1,2,3]) # multidimensional arrays can also be used
    a = np.random.rand(5)
    a, '\n'
    a[indices]

# indexing using boolean arrays
    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    mean = a.mean()
    # for loop could be used to look for all values less than the mean
    # or masking can be used to boolean compare directly
    a[a<mean]

# arithmetic operations on arrays
    a = np.array([(1,2,3,4,5), (10,20,30,40,50)])
    b = np.array([(100,200,300,400,500), (1,2,3,4,5)], dtype='f')
    a
    a * 2
    a / 2.0
    a + b
    a * b # multiplies each element together
    print a / b



if __name__ == "__main__":
    test_run()
