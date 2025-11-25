
number = int(input("Enter a Six digit number: "))

d1 = number//100000
d2 = number//10000%10
d3 = number//1000%10
d4 = number//100%10
d5 = number//10%10
d6 = number%10

sum_digit = d1+d2+d3+d4+d5+d6
print(sum_digit)