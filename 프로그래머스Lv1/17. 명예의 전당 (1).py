def solution(k, score):
    temp = []
    answer = []

    for s in score:
        if len(temp) < k:
            temp.append(s)
        else:
            if s > min(temp):
                temp.remove(min(temp))
                temp.append(s)
        answer.append(min(temp))
    return answer
