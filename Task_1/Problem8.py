"""
    Write a Python program that checks if a given word is a palindrome. A palindrome is a word that reads the same backward as forward.
    Input: "level"
    Output: "The word 'level' is a palindrome."

    Input: "python"
    Output: "The word 'python' is not a palindrome."
"""

word = input()

l , r = 0, len(word) - 1

is_palindrome = True

while l < r:
    if word[l] != word[r]:
        is_palindrome = False
        break
    l += 1
    r -= 1

print(f"\"The word '{word}' is a palindrome.\"" if is_palindrome else f"\"The word '{word}' is not a palindrome.\"")