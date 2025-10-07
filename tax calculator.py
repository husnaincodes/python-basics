
income = int(input("Enter your income : "))

if income<= 5000:
    print("NO TAX")
elif income == 5001 or income <= 10000:
    print("10% Tax")
    print(f"Income after tax is : {income*0.10}")

elif income==1001 or income<= 20000:
    print(" 20% Tax")
    print(f"Income after tax is : {income*0.20}")
elif income>20000:
    print("30% Tax")
    print(f"Income after tax is : {income*0.30}")