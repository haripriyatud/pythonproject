lambda_sum = lambda a, b: a + b

print_color_lambda = lambda color='green': color

print_Details_lambda = lambda name, age: f'my name is {name} and age is {age}'


def calculation(n):
    return lambda a: a ** n


square = calculation(2)
cube = calculation(3)

