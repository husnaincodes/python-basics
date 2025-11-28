def cubes(lst):
    dictionary = {x: x**3 for x in lst}
    return dictionary

print(cubes([1, 2, 3]))
