from functools import reduce


def multiply_by_two(item):
    return item * 2


def capitalize(item):
    return item.capitalize()


def even_numbers_list(item):
    return item % 2 == 0


def name_list_starting_with_s(item):
    return item[0].startswith("S") or item[0].startswith("s")


def filter_leap_year(item):
    return item % 400 == 0 or item % 4 == 0 and item % 100 != 0


def sum_elements(item, elem_sum):
    return item + elem_sum


def passed_score(score):
    return score > 50


my_list = range(1, 11)
name_list = ["radha", "saradha", "prem", "saravan", "santhi", "tanya"]
year_list = [2000, 2015, 2016, 1998, 1999, 2020, 1980, 1900]
phone_number_list = ["6788912357", "9781234612", "8681686846", "6868686854", "67890456890", "9898043411"]
email_list = ["radha@gmail.com", "saradha@gmail.com", "prem@gmail.com", "saravan@gmail.com", "santhi@gmail.com",
              "tanya@gmail.com"]
score_list = [78, 90, 45, 89, 56, 34]

print(list(map(multiply_by_two, my_list)))

print(list(filter(even_numbers_list, my_list)))

print(list(filter(name_list_starting_with_s, name_list)))

print(list(filter(filter_leap_year, year_list)))

print(list(zip(name_list, email_list, phone_number_list)))

print(list(zip(name_list, score_list)))

print(f'sum of the elements in the list: {reduce(sum_elements, my_list, 0)}')

print(list(map(capitalize, name_list)))

print(list(filter(name_list_starting_with_s, map(capitalize, name_list))))

print(list(filter(passed_score, score_list)))

print(f'The passed students with their scores {list(zip(name_list, filter(passed_score, score_list)))}')
