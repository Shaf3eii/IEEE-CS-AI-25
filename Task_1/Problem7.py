"""
    Write a Python program that takes a positive integer as input and finds its prime factors.
    Input: 36
    Output: Prime Factors: 2, 3    
"""

number = int(input())

prime_factors = []

for i in range(2, number):
    if number % i == 0:
        while number % i == 0:
            number /= i
        prime_factors.append(i)
    
print("Prime Factors are: ", end=" ")

i = 0
while i < len(prime_factors) - 1:
    print(f"{prime_factors[i]},", end=" ")
    i += 1

print(prime_factors[i])