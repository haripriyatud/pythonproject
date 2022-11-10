my_set = { 56, 78, 34, 89, 23, 90}
print(my_set)  # {34, 23, 56, 89, 90, 78}
my_set.add(45)
print(my_set)  # {34, 23, 56, 89, 90, 45, 78}
my_set.add(23)
print(my_set) # {34, 23, 56, 89, 90, 45, 78}

my_list = [56, 89, 45, 67, 78, 90, 56, 89]

print(list(set(my_list)))  # [67, 45, 78, 56, 89, 90]

my_set.clear()

print(my_set)  # empty set

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}

C = A.difference(B)
print(C)  # {1, 2, 3}

D = A.intersection(B)

print(D)  # {4, 5}

E = A.union(B)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(E)
A.discard(5)
print(A)  # {1, 2, 3, 4}

A.difference_update(B)
print(A) # {1, 2, 3}
