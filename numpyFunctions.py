# numpy is the general purpose array processing package. it performs high performance multidimenational array object, and tools for working with these arrays. it is the fundamental package for the scientific computing with python.

import numpy as np
my_lst = [1, 2, 3, 4, 5]
arr = np.array(my_lst)

# print(type (arr))
# print(arr.shape)


my_lst1 = [1, 2, 3, 4, 5]
my_lst2 = [2, 3, 4, 5, 6]
my_lst3 = [9, 7, 6, 8, 9]

arr2 = np.array([my_lst1, my_lst2, my_lst3])
print(arr2)
print(arr2.shape)
print(arr2.reshape(1, 15))

# indexing

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[3])



