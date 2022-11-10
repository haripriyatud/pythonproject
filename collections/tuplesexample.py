# tuple creation
employee_names_tuple = ("Alice",'Bob','Charlie','Daniel','Esther','Bob','Fedrik')

# length of tuple
print(len(employee_names_tuple))

# count of a particular element in tuple
print(employee_names_tuple.count('Bob'))

# assessing element of index 1 
print(employee_names_tuple[1])

# assessing last element from tuple- negative indexing
print(employee_names_tuple[-1])

# slicing operation of tuple
print(employee_names_tuple[2:5])

# adding data to a tuple- method 1
new_employee= ('Gabriel',)
employee_names_tuple+=new_employee
print(employee_names_tuple)

# adding more employees to a list
new_employees= ('Harry','Ian')
employee_names_tuple+=new_employees
print(employee_names_tuple)

# adding data to a tuple - method 2 - using lists
list_from_tuple= list(employee_names_tuple)
list_from_tuple.append('Jensi')
employee_names_tuple= tuple(list_from_tuple)
print(employee_names_tuple)

# sorting the employee names tuple in ascending order
sorted_employee_names= sorted(employee_names_tuple)
print(sorted_employee_names)

# sorting the employee names tuple in descending order
sorted_employee_names_descending= sorted(employee_names_tuple,reverse=True)
print(sorted_employee_names_descending)








