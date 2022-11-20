import unittest
from functools import reduce

import functional_programming_example


class MyTestCase(unittest.TestCase):
    phone_number_list = ["6788912357", "9781234612", "8681686846", "6868686854", "67890456890", "9898043411"]
    email_list = ["radha@gmail.com", "saradha@gmail.com", "prem@gmail.com", "saravan@gmail.com", "santhi@gmail.com",
                  "tanya@gmail.com"]
    score_list = [78, 90, 45, 89, 56, 34]

    def test_multiply_by_two(self):
        my_list = range(1, 11)
        self.assertEqual(list(map(functional_programming_example.multiply_by_two,
                                  my_list)), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_even_numbers_list(self):
        my_list = range(1, 11)
        self.assertEqual(list(filter(functional_programming_example.
                                     even_numbers_list,
                                     my_list)), [2, 4, 6, 8, 10])

    def test_names_starting_with_s(self):
        name_list = ["radha", "saradha", "prem", "saravan", "santhi", "tanya"]
        self.assertEqual(list(filter(functional_programming_example.name_list_starting_with_s,
                                     name_list)), ['saradha', 'saravan', 'santhi'])

    def test_filter_leap_year(self):
        year_list = [2000, 2015, 2016, 1998, 1999, 2020, 1980, 1900]
        self.assertEqual(list(filter(functional_programming_example.filter_leap_year,
                                     year_list)), [2000, 2016, 2020, 1980])

    def test_list_sum(self):
        my_list = range(1, 11)
        self.assertEqual(reduce(functional_programming_example.sum_elements, my_list, 0), 55)

    def test_zip_example(self):
        name_list = ["radha", "saradha", "prem", "saravan", "santhi", "tanya"]
        score_list = [78, 90, 45, 89, 56, 34]
        self.assertEqual(list(zip(name_list, score_list)),
                         [('radha', 78), ('saradha', 90), ('prem', 45), ('saravan', 89)
                             , ('santhi', 56), ('tanya', 34)])

    def test_zip_passed_students(self):
        name_list = ["radha", "saradha", "prem", "saravan", "santhi", "tanya"]
        score_list = [78, 90, 45, 89, 56, 34]
        self.assertEqual(list(filter(lambda tup: tup[1] > 50, zip(name_list, score_list))),
                         [('radha', 78), ('saradha', 90), ('saravan', 89), ('santhi', 56)] )


if __name__ == '__main__':
    unittest.main()
