"""
    Write a function that takes two sets as input and returns a new set containing the common elements.
"""

def intersect(s1, s2):
    return set(s1 & s2)


set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

common_elements = intersect(set1, set2)

print(common_elements)
