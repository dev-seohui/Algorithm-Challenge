
def solution(n):
    
    lst = list(str(n))
    new_lst = sorted(lst, reverse=True)
    answer = "".join(new_lst)
    
    return int(answer)
