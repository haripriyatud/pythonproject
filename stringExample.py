a="this is a string"

print(type(a))

b="STRING"

print(len(a))

print(a.upper())

print(b.lower())

print(a.title())

print(a.capitalize())

print(a.find('a'))

print(a.replace('this','the given variable'))

print(a.endswith('string'))

print(a.find('string'))

print(a.count('s'))

print(a.center(20))

price_tag= 'This article costs {price:.2f} euros'

print(price_tag.format(price=56.89))