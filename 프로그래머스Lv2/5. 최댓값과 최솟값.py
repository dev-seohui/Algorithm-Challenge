
def solution(s):
    
    split_s = s.split()
    new_s = [int(x) for x in split_s]
    min_s = str(min(new_s))
    max_s = str(max(new_s))
    print(min_s, max_s)
    answer = min_s + " " + max_s
    return answer
