
num = int(input("Enter the number please :"))

for i in range(2 ,num):

    if num%i==0:

        print("It is not a prime number")
              
        break
else:
    print("It is a prime number")
