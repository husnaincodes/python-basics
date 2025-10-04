
num = int(input("Enter the dividend : "))
num2 = int(input("Enter the divisor : "))


qoutient = num//num2
remainder = num%num2
print(f"Qoutient is : {qoutient} ")
print(f"Remainder is : {remainder}")

condition = (num2*qoutient)+remainder
print(f"Verfication of condition : {condition}")

if num == condition:
    print("Dividend eaqual to condition")
else:
    print("Not equal condition")