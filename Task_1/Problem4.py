"""
    Write a Python program that takes a sentence as input and prints the sentence with each word reversed.
    Ex:
    Input: "Hello World"
    Output: "olleH dlroW"
"""

sentence = input()

l , r = 0, 0
while r < len(sentence):
    if sentence[r] == ' ':
        i = r - 1
        while i >= l:
            print(sentence[i], end="")
            i -= 1
        print(end = " ")
        l = r + 1
    r += 1
else:
    i = r - 1
    while i >= l:
        print(sentence[i], end="")
        i -= 1

print()