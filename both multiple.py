
number1 = int(input("Enter the first number: "))

number2 = int(input("Enter the second number: "))

if(number1%number2==0)or (number2%number1==0):
    print("Both are multiple of each other")
else:
    print("Multiple not!!")