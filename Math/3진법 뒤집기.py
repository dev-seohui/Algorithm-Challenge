def to_ternary(n):
    if n == 0:
        return 0
    ternary = ""
    while n>0:
        ternary = str(n%3) + ternary
        n = n//3
    return ternary

def solution(n):
    num = to_ternary(n)
    new_num = num[::-1]
    result = int(new_num, 3)
    return result
