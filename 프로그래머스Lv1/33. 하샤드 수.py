
def solution(x):
    
    lst = [int(i) for i in str(x)]
    sum_lst = sum(lst)
    
    if x%sum_lst == 0:
        return True
    else:
        return False
