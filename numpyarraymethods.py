import numpy as np

numpyList = np.random.randint(0, 500, 20)

print(numpyList)
numpyList_copy = numpyList.copy()
print(numpyList[4:9])
numpyList[4:9] = -10

print(numpyList)

slicingList = numpyList_copy[:]

print(slicingList)
slicingList[:] = -11

print("Son")
print(numpyList)
print(numpyList_copy)
print(slicingList)


