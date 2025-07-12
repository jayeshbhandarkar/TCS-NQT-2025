"""
Given a string S, find:
1. The first non-repeating character in S (or "None" if none exists).
2. The most frequent character (or the first character if all are unique).

If the string is empty then print invalid input 

Input 1: swadesh
Output 1: w s

Input 2: aabbcc
Output 2: None a
"""

def find_chars(s):
    if not s:  
        print("Invalid input")
        return
    
    for ch in s:
        if s.count(ch) == 1:
            first_non_repeating = ch
            break

    else:
        first_non_repeating = "None"

    most_frequent = max(s, key = s.count)
    print(first_non_repeating, most_frequent)

s = input().strip()
find_chars(s)
