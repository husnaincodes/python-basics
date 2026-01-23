fruits = ["apple","banana","apple","mango","banana"]
my_set = set(fruits)

my_tuple = tuple(my_set)
print(len(my_tuple))

if "orange" in my_tuple:
    print("Exist")
else:
    print("Not Exist")