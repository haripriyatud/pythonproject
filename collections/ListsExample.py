fruitlist = ["pineapple", "apple", "mango"]

berrieslist = ["strawberry", "blackberry", "rasberry", "blueberry"]

print(type(fruitlist))

print('pineapple' in fruitlist)

print('grapes' in fruitlist)

print('grapes' not in fruitlist)


def iterate_list_first_method():
    for i in fruitlist:
        print(i)


iterate_list_first_method()


def iterate_list_second_method():
    print("Iteration using range function")
    for i in range(len(fruitlist)):
        print(fruitlist[i])


iterate_list_second_method()


def iterate_list_third_method():
    print("List comprehension")
    [print(i) for i in fruitlist]


iterate_list_third_method()


def iterate_list_fourth_method():
    for i, val in enumerate(fruitlist):
        print(i, ",", val)


iterate_list_fourth_method()

print(f'The first element the list is {fruitlist[0]}')

print(f'The first last the list is {fruitlist[-1]}')

fruitlist.append('orange')

print(f'The elements in the list after appending an element:  {fruitlist}')

fruitlist.insert(2, 'grapes')

print(f'The elements in the list after inserting an element at position 2:  {fruitlist}')

fruitlist.extend(berrieslist)

print(f'The elements in the list after extending berries list:  {fruitlist}')

fruitlist.pop()

print(f'The elements in the list after removing the last element:  {fruitlist}')

fruitlist.remove('blackberry')

print(f'The elements in the list after removing blackberry:  {fruitlist}')

fruitlist.pop(1)

print(f'The elements in the list after removing the first element:  {fruitlist}')

print(f'slicing the elements in the list')

print(fruitlist[2:5])

print(f'sorting the elements')
fruitlist.sort()
print(f'The elements after sorting:  {fruitlist}')

fruitlist.reverse()
print(f'The elements after reversing:  {fruitlist}')

num_list = [20, 10, 20, 5, 70, 45]

print(num_list.count(20))

num_list.sort()

print(f'The elements after sorting:  {num_list}')

doubled_numbers = [2 * x for x in num_list]

print(doubled_numbers)

odd_numbers = [x for x in num_list if x % 2 != 0]

print(odd_numbers)
