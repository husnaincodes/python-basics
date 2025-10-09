
operator = input("Select one operator(+,-,*,/,%): ")
num = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

if operator=="+":
    print(f"Sum : {num+num2}")
elif operator == "-":
    print(f"Subtraction :{num-num2}")
elif operator=="/":
    print(f"Dividsion: {num//num2}")
elif operator == "*":
    print(f"Multiplication : {num*num2}")
elif operator =="%":
    print(f"Remainder: {num%num2}")