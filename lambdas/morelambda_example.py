from functools import reduce

my_list = range(1, 11)

name_list = ["radha", "saradha", "prem", "saravan", "santhi", "tanya"]

score_list= [67, 78, 34, 45, 89, 53]
email_list = ["radha@gmail.com", "saradha@gmail.com", "prem@gmail.com", "saravan@gmail.com", "santhi@gmail.com",
              "tanya@gmail.com"]

list_before_sorting = [(0, 2), (4, 5), (7, 3), (9, 6)]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 == 0, my_list)))

print(f'sum of the elements in the list: {reduce(lambda item, elem_sum: item+elem_sum, my_list)}')

print(list(map(lambda item: item**2, my_list)))

list_before_sorting.sort(key=lambda x: x[1])

zipped_result = list(zip(name_list, email_list, score_list))

zipped_result.sort(key=lambda x: x[2])

print(zipped_result)
