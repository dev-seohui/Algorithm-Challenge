
def solution(want, number, discount):
    answer = 0
    length1 = sum(number)
    length2 = len(discount)
    diff = length2 - length1+1
    print(diff)
    for i in range(diff):
        new_number = number[:]
        for d in discount[i:i+length1]:
            if d in want and new_number[want.index(d)] > 0:
                new_number[want.index(d)] -= 1
        if sum(new_number) == 0:
            answer += 1
    return answer
