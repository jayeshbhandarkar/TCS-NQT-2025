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
