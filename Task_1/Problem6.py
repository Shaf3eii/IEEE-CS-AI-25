"""
    Write a Python program that takes a positive integer as input and checks whether it is a perfect number or not. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
    Ex:
    Input: 28
    Output: 28 is a perfect number. 
"""

number = int(input())

sum = 1 if number != 1 else 0 # here i assumed that 1 is not perfect since i'm the only one who is perfect :)

i = 2
while i * i < number:
    if number % i == 0:
        sum += i
        sum += number / i
    i += 1

print(f"{number} is a perfect number." if sum == number else f"{number} is not a perfect number")