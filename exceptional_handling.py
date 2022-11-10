#Example1:

person_dict={'Alice':56,'Bob':67,'Charlie':34}
print(person_dict)

try:
    name = input('Enter a name from the above dictionary to get the age:')
    age = person_dict[name]
    print(age)
except KeyError:
    print(f'The name {name} is not found in the dictionary')


#Example2
numbers_list = [23,78,89]
try:
    index = input('Enter the index of an element needed to be retrived:')
    num= numbers_list[index]
    print(num)
except TypeError:
    print("Index is not integer")
except IndexError:
    print('Index is not in range')

#Example3

try:
    f = open("file.txt") 
except:
    print("File not found")
finally:
    print("operation completed sucessfully")


#Example 4:
try:
    #x=10
    a = x + 5
except NameError:
    print(f'The variable x is not defined')
else:
    print(a)


#Example5:

age = int(input('Please enter your age:'))
if age<0 or age >100:
      raise Exception("Sorry, age is not within the correct range")









