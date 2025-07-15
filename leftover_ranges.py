def find_leftover_ranges(L, U, A):
    A = set(A)  
    missing_ranges = []
    start = None
    
    for num in range(L, U + 1):
        if num not in A:
            if start is None:
                start = num  
        else:
            if start is not None:
                missing_ranges.append([start, num - 1])  
                start = None
    
    if start is not None:  
        missing_ranges.append([start, U])
    
    return missing_ranges

input1 = list(map(int, input().strip("[]").split(",")))
print(find_leftover_ranges(input1[0], input1[1], input1[2:]))
