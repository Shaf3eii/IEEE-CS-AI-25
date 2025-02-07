"""
    Create a program that reads a text file, counts the occurrences of each word, and prints the results.
"""

file_name = "/media/mahmoud-elshafei/New Volume/My_Github/IEEE-CS-AI-25/Task_2/simple_text.txt"
word_count = {}


with open(file_name, 'r') as file_object:
    one_line = ''
    for line in file_object:
        one_line += line.rstrip() + ' '
    
    word = ''
    for letter in one_line:
        if not letter.isalpha():
            word_count[word] = word_count.get(word, 0) + 1 
            word = ''
            continue
        word += letter
    
    if word:
        word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word:<10}: {count}") # feh imposter 3bara 3n           : 26 bs m4 3aref eh dh wallahy