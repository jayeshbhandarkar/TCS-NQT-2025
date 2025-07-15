def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

def digit_root(num):
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num

def compute_result(m, n):
    mth_prime = find_nth_prime(m)
    nth_prime = find_nth_prime(n)
    
    m1 = digit_root(mth_prime)
    n1 = digit_root(nth_prime)
    
    return mth_prime * m1

m = int(input())
n = int(input())
result = compute_result(m, n)
print(result)
