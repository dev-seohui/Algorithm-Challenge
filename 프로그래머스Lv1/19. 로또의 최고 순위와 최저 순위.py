
# 첫번째 풀이
def solution(lottos, win_nums):
    
    min_rank, max_rank = 7, 7
    for i in range(len(lottos)):
        if lottos[i] == 0:
            max_rank -= 1
        elif lottos[i] in win_nums:
            min_rank -= 1
            max_rank -= 1
    return min(max_rank, 6), min(min_rank, 6)



# 두번쨰 풀이
def solution(lottos, win_nums):
    answer = []
    result = [0, 0]

    dup = len(set(lottos) & set(win_nums))  # 중복값 개수
    zero = lottos.count(0)                  # 0의 개수 

    count1 = dup                            # 최소
    count2 = dup + zero                     # 최대

    if count1 == 0:
        if count2 == 0:
            result[0] = result[1] = 6
        else:
            result[0] = 7 - count2
            result[1] = 6
    else:
        result[0] = 7 - count2
        result[1] = 7 - count1

    return result
