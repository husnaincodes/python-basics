
friends  = ["husnain",34 , 4.561 ,"GAARA" ,"thorfin", False]

print(friends)

print(friends[0:2])
print(friends[0:4])
print(friends[0:5])

friends[0]= 'shahbaz'
print(friends[0])

friends.append("RAYAY")
print(friends)


list = [23,45,78,90,56,34]
list.sort()
print(list)



my_list = [67,44,57,89,59,0,4]
my_list.insert(5,99)
# my_list.sort()
my_list.reverse()

print(my_list)

list2 = [ "1" , 2,3,4,5,6,7,8,9]
# c.clear()
list2.remove(4)
print(list2)





copy = [34,56,78,99,00,11,33]
print(copy)
mylist = copy.copy()
print(mylist)

count = [1,1,3,3,4,4,5,5,5,5,5,5,5,5,3,3,3,3,3,6,6,]
# e.count(3) incorrect
print(count.count(3))