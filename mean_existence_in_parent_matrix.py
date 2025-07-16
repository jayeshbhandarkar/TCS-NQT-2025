def check_mean_exists(matrix, m, n):
    elements_set = set()
    for row in matrix:
        elements_set.update(row)
    
    for top in range(m):
        for left in range(n):
            for bottom in range(top, m):
                for right in range(left, n):
                    total = 0
                    count = 0
                    for i in range(top, bottom + 1):
                        for j in range(left, right + 1):
                            total += matrix[i][j]
                            count += 1
                    mean = total / count
                    if mean in elements_set:
                        print(f"Elements exist mean {int(mean)} : True")
                        return
    print("Elements exist mean : False")

m, n = map(int, input().split())
matrix = []

for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

check_mean_exists(matrix, m, n)
