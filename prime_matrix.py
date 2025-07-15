def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_matrix():
    try:
        m, n = map(int, input().split())
        if m <= 0 or n <= 0:
            print("Wrong Input")
            return

        elements = list(map(int, input().split()))
        if len(elements) != m * n:
            print("Wrong Input")
            return
        if any(x < 0 for x in elements):
            print("Wrong Input")
            return

        for i in range(m):
            row = elements[i*n : (i+1)*n]
            if not any(is_prime(x) for x in row):
                print("Not Valid")
                return

        print("Valid")
        
    except:
        print("Wrong Input")

check_matrix()
