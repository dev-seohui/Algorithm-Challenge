def solution(answers):
    length = len(answers)
    result = []
    answer = []
    
    no1 = "12345" * (length//5 + 1)
    no2 = "21232425" * (length//8 + 1)
    no3 = "3311224455" * (length//10 + 1)
    
    sol1 = sol2 = sol3 = 0
    
    for i in range(length):
        if answers[i] == int(no1[i]):
            sol1 += 1
        if answers[i] == int(no2[i]):
            sol2 += 1
        if answers[i] == int(no3[i]):
            sol3 += 1
    
    result.extend([sol1, sol2, sol3])
    max_score = max(result)
    answer = [x+1 for x in range(3) if result[x] == max_score]
    
    return sorted(answer)
