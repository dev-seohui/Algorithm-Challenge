def solution(array, commands):
    answer = []
    for c in commands:
        part = array[c[0]-1:c[1]]
        part.sort()
        answer.append(part[c[2]-1])
    return answer
