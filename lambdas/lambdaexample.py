lambda_sum = lambda a,b : a+b

print(type(lambda_sum))

print(lambda_sum(4,6))

print_color_lambda = lambda color='green':  print(color)

print_color_lambda('blue')

print_color_lambda()


printyourDetails_lambda = lambda name,age :  print(f'my name is {name} and age is {age}')

printyourDetails_lambda(name="George",age=45)

printyourDetails_lambda(age=45,name="Sam")

def calculation(n):
  return lambda a : a**n

square = calculation(2)
cube = calculation(3)

print(square(2))
print(cube(2))

