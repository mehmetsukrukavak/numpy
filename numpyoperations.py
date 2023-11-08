import numpy as np

array = np.random.randint(0, 200, 10)

print(array)

result_array = array > 100

print(result_array)
print(array[result_array])
print(array.mean()) #ortalama
print(np.mean(array)) #ortalama
print(np.sqrt(array)) #karekök
