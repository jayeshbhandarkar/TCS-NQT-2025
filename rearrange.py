def rearrange(arr):
    n = len(arr)
    for i in range(0, n - 1, 2):
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

arr = list(map(int, input().split()))
print(rearrange(arr))
