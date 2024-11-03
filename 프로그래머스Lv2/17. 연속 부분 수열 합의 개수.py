
def solution(elements):
    answer = set()
    n = len(elements)
    
    for i in range(1, n+1):
        for j in range(n):
            total = 0
            for k in range(i):
                total += elements[(j+k)%n]
            answer.add(total)
    print(answer)
    return len(answer)
