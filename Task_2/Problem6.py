"""
    Generate a random password of 8 characters, including a mix of uppercase letters, lowercase letters, and numbers.
"""

from random import sample
from string import ascii_letters, digits

mix_string = ascii_letters + digits
mix_list = list(mix_string)

password = ''
generate = sample(mix_list, 8)

for p in generate:
    password += p

print(password)