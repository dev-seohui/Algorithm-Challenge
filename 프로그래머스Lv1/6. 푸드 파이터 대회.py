def solution(food):
    answer = ''
    
    for i in range(len(food)):
        value = food[i]//2
        if value > 0:
            answer += str(i)*value
    answer += '0' + answer[::-1]
    return answer
