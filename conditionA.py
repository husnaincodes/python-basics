
number = int(input("Enter the number : "))
if number%2==0 and number%3==0:
    print(f"Number is divible by both 2/3 : {number}")
elif number%2==0:
    print("This number is only divide by 2")
elif  number%3 ==0:
    print("This number  is only divide by 3 ")
else:
    print("This number is not divible by 2/3")