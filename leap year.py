year = int(input('Enter the year :'))
if (year%400==0) or (year%4==0 and year % 100 != 0):

    print('This is a leap year')
else:
    print("It is not a leap year")
    