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


