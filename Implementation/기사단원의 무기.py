def solution(number, limit, power):
    
    answer = [0]*(number+1)
    result = 0
    
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            answer[j] += 1
    
    for i in answer:
        if i > limit:
            result += power
        else:
            result += i
    return result
