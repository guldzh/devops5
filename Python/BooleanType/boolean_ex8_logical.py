#  Leap Year
# A year is leap if it is divisible by 4 but not by 100 
# unless it is also divisible by 400. 
# Write a program that takes a year as input 
# and prints True if it's a leap year, False otherwise.

year=int(input("Please enter the year: "))

is_divisible_4=year%4==0
is_divisible_100=year%100!=0
is_divisible_400=year%400==0

is_leap_year=is_divisible_4 and is_divisible_100 or is_divisible_400 

print("Given ",year,"is a leap year?",is_leap_year)


