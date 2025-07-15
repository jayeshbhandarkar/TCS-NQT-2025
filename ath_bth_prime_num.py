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

def prime_multiplication_minus_one(a, b):
    prime_a = find_nth_prime(a)
    prime_b = find_nth_prime(b)
    return (prime_a * prime_b) - 1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(prime_multiplication_minus_one(a, b))
