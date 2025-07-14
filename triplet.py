def min_steps_to_equal(P, Q, R):
    arr = [P, Q, R]
    arr.sort()

    if arr[0] == arr[1] == arr[2]:
        return 0
    
    steps= 0

    while True:
        arr[0] += 1
        arr[1] += 1
        arr[2] -= 1
        steps += 1
        arr.sort()

        if arr[0] == arr[1] == arr[2]:
            return steps
        
        if (arr[0] == arr[1] and arr[1]+1 == arr[2]) or (arr[1] == arr[2] and arr[0]+1 == arr[1]):
            return -1

T = int(input())
for _ in range(T):
    P, Q, R = map(int, input().split())
    print(min_steps_to_equal(P, Q, R))
