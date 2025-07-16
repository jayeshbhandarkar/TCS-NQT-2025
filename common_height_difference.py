def find_common_difference(heights):
    if any(h < 0 for h in heights):
        return "Not valid inputs"

    diff1 = heights[1] - heights[0]
    diff2 = heights[2] - heights[1]
    diff3 = heights[3] - heights[2]

    if diff1 == diff2 or diff1 == diff3:
        return diff1
    elif diff2 == diff3:
        return diff2
    else:
        return "None"

input_data = list(map(int, input().split()))
print(find_common_difference(input_data))
