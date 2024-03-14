def solution(d, budget):
    d.sort(reverse=False)
    result = 0
    total = 0
    for i in range(len(d)):
        if budget >= d[i] :
            budget = budget - d[i]
            result += 1
    return result
