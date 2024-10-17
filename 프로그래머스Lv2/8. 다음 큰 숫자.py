
def solution(n):
    answer = 0
    count1 = bin(n).count("1")

    next_num = n + 1
    while True:
        count2 = bin(next_num).count("1")
        if count1 == count2:
            return next_num
        next_num += 1
