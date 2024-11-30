def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for t in tangerine:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    
    for size, count in sorted_dic:
        k -= count
        answer += 1
        if k <= 0:
            break
    return answer
