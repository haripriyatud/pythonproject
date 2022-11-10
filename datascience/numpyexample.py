import random
import numpy as np

numbers = np.array(random.sample(range(0, 10), 5))

print(numbers)

print(type(numbers))

print(numbers.ndim)

print(numbers.shape)

sorted_array= np.sort(numbers)

print(sorted_array)

sorted_descending_array= sorted_array[::-1]

print(sorted_descending_array)

print(np.min(numbers))

print(np.max(numbers))

print(np.sum(numbers))

print(np.mean(numbers))

even_numbers = np.arange(2,20,2)

print(even_numbers)

new_shaped_array = even_numbers.reshape(3,3)

print(new_shaped_array)

print(new_shaped_array.shape)

print(new_shaped_array.ndim)

array1= np.array([1,6,7])

array2= np.array([5,7,8])

concat_array= np.concatenate((array1,array2))

print(concat_array)

arr = np.array([6,8,2,1,9,45,23,3])

filter_divisible_by_3 = arr % 3 == 0

filteredarr = arr[filter_divisible_by_3]

print()
print(filteredarr)




