from array import *
my_array=array('i',[1,2,3,4,5])
for i in my_array:
     print(i)

my_array.insert(0,7)
print(my_array)
my_array1=array('i',[12,10,11])
my_array.extend(my_array1)
print(my_array)
temp=[98,97,96]
my_array.fromlist(temp)
print(my_array)

import numpy as np

# Creating a 2D array (matrix)
twoDArray = np.array([
    [11, 15, 10, 6],  # Day 1
    [10, 14, 11, 5],  # Day 2
    [12, 17, 12, 8],  # Day 3
    [15, 18, 14, 9]   # Day 4
])
print(twoDArray)