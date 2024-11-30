def solution(babbling):
    available = ["aya", "ye", "woo", "ma"]
    not_available = ["ayaaya", "yeye", "woowoo", "mama"]
    answer = 0
    
    for b in babbling:
        is_not_available = False
        for n in not_available:
            if n in b:
                is_not_available = True
                break
        if is_not_available:
            continue
        for a in available:
            b = b.replace(a, " ")
        if b.strip() == "":
            answer += 1          
    return answer
