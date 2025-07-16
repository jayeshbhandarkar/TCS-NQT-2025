m, n = map(int, input().split())

matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(m):
    if i % 2 == 0:
        print(*matrix[i])
        
    else:
        print(*matrix[i][::-1])
