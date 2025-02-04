"""
    Write a Python program that takes a positive integer as input and prints the sum of its digits.
    Ex:
    Input: 123
    Output: The sum of digits is 6 (1 + 2 + 3).
"""

number = int(input())
temp = str(number)
sum = 0

while number > 0:
    sum += number % 10
    number //= 10

print(f"The sum of digits is {sum} (", end = "")
idx = 0
while idx < len(temp) - 1:
    print(temp[idx], end=" + ")
    idx += 1

print(f"{temp[idx]}).")