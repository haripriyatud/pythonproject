import operator


class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    def print_person_details(self):
        print(f'Person name is: {self.name}, Person age is {self.age}')


person_list = []

person1 = Person(1, 'Alice', 56)
person1.print_person_details()
person_list.append(person1)

person2 = Person(2, 'Bob', 67)
person2.print_person_details()
person_list.append(person2)

person3 = Person(3, 'Charlie', 78)
person3.print_person_details()
person_list.append(person3)

person4 = Person(4, 'Daniel', 43)
person4.print_person_details()
person_list.append(person4)

person5 = Person(5, 'Emanuel', 29)
person5.print_person_details()
person_list.append(person5)

person6 = Person(6, 'Fredric', 32)
person6.print_person_details()
person_list.append(person6)

person7 = Person(7, 'Grace', 18)
person7.print_person_details()
person_list.append(person7)

person8 = Person(8, 'Haris', 82)
person8.print_person_details()
person_list.append(person8)

person9 = Person(9, 'Jack', 91)
person9.print_person_details()
person_list.append(person9)


person_list.sort(key=operator.attrgetter('age'))

print(f'The oldest person is {person_list[-1].name}')

print(f'The youngest person is {person_list[0].name}')


