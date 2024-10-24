
def solution(t, p):
    length = len(p)
    case = []
    result = 0
    
    for i in range(len(t)-length+1):
        case.append(t[i:i+length])
    
    for i in case:
        if i <= p:
            result += 1
    return result
