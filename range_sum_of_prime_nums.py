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

def sum_of_primes(N, M):
    total = 0
    for num in range(N, M + 1):
        if is_prime(num):
            total += num
    return total

N = int(input("Enter N: "))
M = int(input("Enter M: "))

if N > M:
    print("Invalid input! N should be ≤ M.")
else:
    result = sum_of_primes(N, M)
    print(f"Sum of prime numbers from {N} to {M} is: {result}")
    