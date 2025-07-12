def find_unique(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    for i in count:
        if count[i] == 1:
            return i
    
arr = list(map(int, input().strip("[]").split(",")))
print(find_unique(arr))


# def find_unique(arr):
#     for i in arr:
#         if arr.count(i) == 1:
#             return i
#         return None

# arr = list(map(int, input().strip("[]").split(",")))
# print(find_unique(arr))


"""
n = int(input())
arr = list(map(int, input().split()))

unique_element = 0
for num in arr:
    unique_element ^= num
print(unique_element)
"""


# If we want to return all the unique elements from the array
"""
def find_unique(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    result = []
    for i in count:
        if count[i] == 1:
            result.append(i)
        
    return result
    
arr = list(map(int, input().strip("[]").split(",")))
print(find_unique(arr))
"""