
num = int(input("Enter the number please :"))
for i in range(2 ,num):
    if i%num==0:
        print("IT is not a Prime number")
        break
else:
    print("It is a prime number")
