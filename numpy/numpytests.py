import numpy as np

arr1 = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]])

arr2= arr1[:,2] + 100

arr3=arr1[:,1]+200

print(arr1)
print(type(arr1.shape))
print(arr2)
#print(arr3)