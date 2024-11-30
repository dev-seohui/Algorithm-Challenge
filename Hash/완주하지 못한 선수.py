def solution(participant, completion):
    answer = ""

    dic1 = {}
    dic2 = {}
    count1, count2 = 0, 0

    for p in participant:
        dic1[hash(p)] = p
        count1 += hash(p)

    for c in completion:
        dic2[hash(c)] = c
        count2 += hash(c)

    val = count1 - count2
    answer += dic1[val]
    return answer
