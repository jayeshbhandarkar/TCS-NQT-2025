def anagram(s1, s2):
    if not s1 or not s2 or len(s1) != len(s2):
        print("Invalid input")
        return

    for ch in s1:
        if ch not in s2:
            print("False")
            return

    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            print("False")
            return

    print("True")
    return

s1 = input()
s2 = input()
anagram(s1, s2) 


"""
def anagram(s1, s2):
    if not s1 or not s2 or len(s1) != len(s2):
        print("Invalid input")
        return

    if sorted(s1) == sorted(s2):
        print("True")
    else:
        print("False")

s1 = input()
s2 = input()
anagram(s1, s2) 
"""