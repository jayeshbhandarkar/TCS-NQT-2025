def find_minimum_in_matrix():
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        print("Invalid input")
        return

    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    min_val = min(min(row) for row in matrix)
    print(min_val)

find_minimum_in_matrix()
