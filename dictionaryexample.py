person_dict={'Alice':56,'Bob':67,'Charlie':34}

print(type(person_dict))

print(person_dict.get('Alice'))

print(person_dict['Charlie'])
person_dict['Daniel']=45

print(person_dict)

person_dict['Charlie']=35

print(person_dict)

keys=list(person_dict.keys())
print(keys)

values=list(person_dict.values())
print(values)

items = list(person_dict.items())

print(items)

sorted_person_dict = sorted(person_dict.items(), key = lambda x: x[1])

print(sorted_person_dict)



nested_dict_example= {'Alice':{'age':56,'Department':'HR'},'Bob':{'age':67,'Department':'Sales'}}

print(nested_dict_example.keys())

print(nested_dict_example['Alice']['age'])

nested_dict_example['Charlie']={'age':34,'Department':'Production'}

nested_dict_items = list(nested_dict_example.items())

print(nested_dict_items)