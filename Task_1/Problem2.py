"""
    Write a program that takes today’s date and prints the date of the next week.
    Ex:
    Input: 	  Day: 25 Month: 1 Year: 2025
    Output:   Day: 1  Month: 2 Year: 2025
"""

# January March May July August October December -----> 31
# April June September November ----> 30
# Febraury ----> 28

# print(2024 % 4)
# print(2024 % 100)
# 2024 is a leap year :)

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))


increase_month = False

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    new_day = (7 + day) % 31 if 7 + day > 31 else 7 + day
    increase_month +=  7 + day > 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    new_day = (7 + day) % 30 if 7 + day > 30 else 7 + day
    increase_month +=  7 + day > 30
else:
    # if we are in a leap year 
    leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    new_day = (7 + day) % (28 + leap_year) if 7 + day > (28 + leap_year) else 7 + day
    increase_month +=  7 + day > (28 + leap_year)

new_month = month + increase_month
new_year = year

if new_month > 12:
    new_month = 1
    new_year += 1

print(f"Day: {new_day} Month: {new_month} Year: {new_year}")