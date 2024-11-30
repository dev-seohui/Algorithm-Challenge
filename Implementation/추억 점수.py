def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        score = 0
        for i in range(len(name)):
            if name[i] in p:
                score += yearning[i]
        answer.append(score)
    return answer
