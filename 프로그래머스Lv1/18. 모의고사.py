def solution(answers):
    supo1, supo2, supo3 = "12345", "21232425", "3311224455"
    supo1 = supo1*(len(answers)//len(supo1)+1)
    supo2 = supo2*(len(answers)//len(supo2)+1)
    supo3 = supo3*(len(answers)//len(supo3)+1)
    point1, point2, point3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == int(supo1[i]):
            point1 += 1
        if answers[i] == int(supo2[i]):
            point2 += 1
        if answers[i] == int(supo3[i]):
            point3 += 1
    
    lst = [point1, point2, point3]
    max_lst = max(lst)
    result = []
    for i in range(len(lst)):
        if lst[i] == max_lst:
            result.append(i+1)
    return result
