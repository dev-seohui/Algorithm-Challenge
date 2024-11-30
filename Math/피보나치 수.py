def solution(n):
    previous, current = 0, 1
    while n>=2:
        previous, current = current, previous+current
        n -= 1
    return current%1234567
