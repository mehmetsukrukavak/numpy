import numpy as np

#numpy arrays
myList = [10, 20, 30, 40]
print(type(myList))

numpyArray = np.array(myList)

print(type(numpyArray))
print(f"Min -> {numpyArray.min()}")
print(f"Max -> {numpyArray.max()}")
print(f"0 -> {numpyArray[0]}")
numpyArray[0] = 50
numpyArray.sort()
print(f"0 -> {numpyArray[0]}")
print(f"Min -> {numpyArray.min()}")
print(f"Max -> {numpyArray.max()}")


