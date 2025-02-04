"""
    Write a program that takes numbers as input from the user, terminates when the user enters -1, and prints the sum of all the entered numbers.
    Ex:
    Input: 4 8 15 16 23 42 -1
    Output: Sum: 108
"""

sum = 0

while True:
    x = int(input())
    if x == -1: break
    sum += x

print(sum)