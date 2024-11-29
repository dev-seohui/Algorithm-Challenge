
def solution(clothes):
    answer = 1
    dic = {}
    
    for clothe in clothes:
        dic[clothe[1]] = dic.get(clothe[1], 0) + 1
    
    for d in dic.values():
        answer *= (d+1)
    
    return answer-1
