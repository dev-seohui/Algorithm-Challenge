
def solution(x, n):
    answer = [x]*n
    print(answer)
    
    for i in range(n):
        for j in range(i+1, n):
            answer[j] += x
    return answer
  
