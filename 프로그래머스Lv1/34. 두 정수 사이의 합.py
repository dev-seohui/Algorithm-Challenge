
def solution(a, b):
    
    small = min(a, b)
    big = max(a, b)
    diff = big - small + 1
    
    lst = [small + x for x in range(diff)]
    return sum(lst)
