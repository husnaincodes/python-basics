num = int(input("Enter three digit number : "))

sum_digit = (num//100) + (num//10%10) +(num%10)
print(sum_digit)