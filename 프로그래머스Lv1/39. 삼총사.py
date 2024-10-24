
def solution(number):
    
    length = len(number)
    count = 0
    
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                if number[i]+number[j]+number[k] == 0:
                    count += 1
    return count
