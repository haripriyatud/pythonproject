import unittest
import lambdaexample


class MyTestCase(unittest.TestCase):
    def test_lambda_sum(self):
        result = lambdaexample.lambda_sum(2, 3)
        self.assertEqual(result, 5)

    def test_print_color_lambda_green(self):
        color = lambdaexample.print_color_lambda()
        self.assertEqual(color, 'green')

    def test_print_color_lambda_blue(self):
        color = lambdaexample.print_color_lambda('blue')
        self.assertEqual(color, 'blue')

    def test_print_Details_lambda_scenario1(self):
        details = lambdaexample.print_Details_lambda(name="George", age=45)
        self.assertEqual(details, 'my name is George and age is 45')

    def test_print_Details_lambda_scenario2(self):
        details = lambdaexample.print_Details_lambda(age=45, name="Sam")
        self.assertEqual(details, 'my name is Sam and age is 45')

    def test_calculation_square(self):
        square = lambdaexample.calculation(2)
        self.assertEqual(square(2), 4)

    def test_calculation_cube(self):
        cube = lambdaexample.calculation(3)
        self.assertEqual(cube(3), 27)


if __name__ == '__main__':
    unittest.main()
