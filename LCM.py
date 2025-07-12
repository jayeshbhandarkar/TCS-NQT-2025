import math
def find_lcm(a, b):
    gcd_ab = math.gcd(a, b)  
    lcm_ab = (a * b) // gcd_ab
    return lcm_ab

a, b = map(int, input().split())
print(find_lcm(a, b))


"""
def gcd(a, b):
    while b:
        a, b = b, a % b 
    return a

def find_lcm(a, b):
    return (a * b) // gcd(a, b) 

a, b = map(int, input().split())
print(find_lcm(a, b))
"""
