import numpy as np

identity_matrtix= np.identity(3,dtype=int)

mat= np.full((3,3,2),15)


print(mat)
#print(identity_matrtix)


print(mat.shape)

list_of_items= [1,2,3,4,6,78,9,0,-1,3,567]

positive_items= [item for item in list_of_items if item >=0]
print(positive_items)
