def solution(participant, completion):
    part_dic = {}
    comp_dic = {}
    part_total = 0
    comp_total = 0
    answer = ""
  
    for p in participant:
        part_dic[hash(p)] = p
        part_total += hash(p)
    for c in completion:
        comp_dic[hash(c)] = c
        comp_total += hash(c)
    
    value = part_total - comp_total
    answer += part_dic[value]
    return answer
