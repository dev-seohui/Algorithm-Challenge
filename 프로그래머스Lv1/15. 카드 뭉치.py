def solution(cards1, cards2, goal):
    answer = []
    
    for g in goal:
        if len(cards1)>0 and g==cards1[0]:
            answer.append(cards1[0])
            cards1 = cards1[1:]
        elif len(cards2)>0 and g==cards2[0]:
            answer.append(cards2[0])
            cards2 = cards2[1:]
        else:
            return "No"
        
    if answer == goal:
        return "Yes"
    else:
        return "No"
