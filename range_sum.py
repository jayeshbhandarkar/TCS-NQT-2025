# Solution 1

def range_sum(i, j):
    total = 0
    for num in range(i, j + 1):
        total += num
    return total

T = int(input())
for _ in range(T):
    user_input = input()
    values = user_input.split()
    if len(values) < 2:
        print("Invalid input i&j i <= j < 10000")
        continue

    i, j = map(int, values)

    if i >= j or i < 0 or j >= 10000:
        print("Invalid input i&j i <= j < 10000")

    else:
        print(range_sum(i, j), end=" ")


# Solution 2

"""
def range_sum(i, j):
    return (j*(j+1)//2) - (i*(i-1)//2)

T = int(input())
for _ in range(T):
    user_input = input()
    values = user_input.split()
    if len(values) < 2:
        print("Invalid input i&j i <= j < 10000")
        continue

    i, j = map(int, values)

    if i >= j or i < 0 or j >= 10000:
        print("Invalid input i&j i <= j < 10000")

    else:
        print(range_sum(i, j), end=" ")
"""