import numpy as np

myMatrixList = [[1,0,0], [0,1,1], [1, 0, 1],[0, 0, 0]]
print(myMatrixList)
numpyMatrix = np.array(myMatrixList)
print(numpyMatrix)
print(numpyMatrix.shape)

myList = list(range(0, 10))
print(myList)

myNumpyList = np.arange(0, 10)
print(myNumpyList)

print(np.zeros(10))
print(np.zeros((10, 10)))

print(np.ones(10))
print(np.ones((10, 10)))

print(np.linspace(0, 10, 100))

print(np.random.randint(0, 5000, 10))