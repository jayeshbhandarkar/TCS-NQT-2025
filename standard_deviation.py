import math

n = int(input())
arr = list(map(int, input().split()))

if len(arr) != n:
    print("Invalid Input")
else:
    mean = sum(arr) / len(arr)

    squared_diff = [(x - mean) ** 2 for x in arr]
    std_dev = math.sqrt(sum(squared_diff) / len(arr))

    print(f"{std_dev:.2f}")
