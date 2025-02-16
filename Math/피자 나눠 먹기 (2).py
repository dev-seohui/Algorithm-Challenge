def solution(n):
    lcm = (6 * n) // gcd(6, n)
    return lcm // 6     

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
