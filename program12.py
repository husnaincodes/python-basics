A = (1, 2, 3, 4)
my_set1 = set(A)

B= (3, 4, 5, 6)
my_set2 = set(B)

common = my_set1.intersection(my_set2)
print(common)

my_tuple = tuple(common)
print(my_tuple)