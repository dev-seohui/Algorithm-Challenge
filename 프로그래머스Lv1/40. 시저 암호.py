
def solution(s, n):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz" #26자
    
    for i in s:
        if (i != " " and i == i.lower()): 
            num = (alphabet.index(i.lower())+n)%26
            answer += alphabet[num]
        elif (i != " " and i == i.upper()): 
            num = (alphabet.index(i.lower())+n)%26
            answer += alphabet[num].upper()
        else:
            answer += " "
    return answer
    
