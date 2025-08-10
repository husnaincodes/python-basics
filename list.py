
friends  = ["husnain",34 , 4.561 ,"GAARA" ,"thorfin", False]

print(friends)

print(friends[0:2])
print(friends[0:4])
print(friends[0:5])

friends[0]= 'shahbaz'
print(friends[0])

friends.append("RAYAY")
print(friends)


a = [23,45,78,90,56,34]
a.sort()
print(a)



b = [67,44,57,89,59,0,4]
b.insert(5,99)
# b.sort()
b.reverse()

print(b)

c = [ "1" , 2,3,4,5,6,7,8,9]
# c.clear()
c.remove(4)
print(c)





d = [34,56,78,99,00,11,33]
print(d)
mylist = d.copy()
print(mylist)

e = [1,1,3,3,4,4,5,5,5,5,5,5,5,5,3,3,3,3,3,6,6,]
# e.count(3) incorrect
print(e.count(3))