def solution(brown, yellow):
    answer = [0, 0]
    width, height = 0, 0
    
    divisor = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i == 0:
            width, height = max(i, yellow//i), min(i, yellow//i)
            divisor.append([width, height])
    
    for d in divisor:
        if brown == ((d[0]+d[1])*2+4):
            answer[0] = d[0]+2
            answer[1] = d[1]+2
    return answer
