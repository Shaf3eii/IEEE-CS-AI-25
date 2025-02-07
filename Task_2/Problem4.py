"""
Create a dictionary representing a library catalogue. 
    Each book should have a title, author, and publication year.
"""

library = {'الكيبورد العتيق': {'title': 'how to become stupid', 'author': 'ShaFeiii', 'publication year': '1907'},
           'Hello python': {'title': 'how to become autistic', 'author': 'CS', 'publication year': '2023'}}
for book, details in library.items():
    print(f"Book: {book}, Title: {details['title']}, Author: {details['author']}, Year: {details['publication year']}")