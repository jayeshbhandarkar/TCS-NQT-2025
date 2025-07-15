def find_valid_numbers(arr, x, y):
    valid_numbers = []  
    n = len(arr)

    for i in range(n):
        for j in range(n):  
            num = int(str(arr[i]) + str(arr[j])) 
            if x <= num <= y:  
                valid_numbers.append(str(num))

    print(" ".join(valid_numbers))  

n = int(input())
x = int(input())
y = int(input())
arr = list(map(int, input().strip("[]").split(",")))
find_valid_numbers(arr, x, y)
