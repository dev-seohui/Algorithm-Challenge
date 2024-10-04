def solution(s):
    answer = []

    for i in range(len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            answer.append(i - s.rfind(s[i], 0, i))

    return answer
