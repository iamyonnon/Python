import numpy as np

myList2 = [1, 2, 3]
myList3 = [4, 5, 6]

myArray2 = np.array(myList2)
myArray3 = np.array(myList3)
print(myArray2 + myArray3)
#when array, they will add everything together

print(myArray2.dot(myArray3));
#method dot will add and multiply value