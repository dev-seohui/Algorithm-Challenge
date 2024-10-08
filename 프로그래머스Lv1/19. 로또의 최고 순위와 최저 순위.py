
def solution(lottos, win_nums):
    
    min_rank, max_rank = 7, 7
    for i in range(len(lottos)):
        if lottos[i] == 0:
            max_rank -= 1
        elif lottos[i] in win_nums:
            min_rank -= 1
            max_rank -= 1
    return min(max_rank, 6), min(min_rank, 6)

