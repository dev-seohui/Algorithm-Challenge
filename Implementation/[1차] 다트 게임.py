def solution(dartResult):
    answer = []
    i = 0
    while i < len(dartResult):
        if i + 1 < len(dartResult) and dartResult[i+1].isdigit():
            score = int(dartResult[i:i+2]) 
            i += 2
        else:
            score = int(dartResult[i])  
            i += 1
        
        bonus = dartResult[i]
        if bonus == 'S':
            score = score ** 1
        elif bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
        i += 1
        
        if i < len(dartResult) and (dartResult[i] == '*' or dartResult[i] == '#'):
            if dartResult[i] == '*':
                score *= 2
                if answer:
                    answer[-1] *= 2  
            elif dartResult[i] == '#':
                score *= -1
            i += 1

        answer.append(score)
    return sum(answer)


*** 참고하면 좋을 코드 ***
def solution(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)
