
def solution(s):
    answer = ""
    
    lst = list(s)
    
    for i in lst:
        if i == " ":
            answer += " "
        elif i in "1234567890":
            answer += i
        else:
            if not answer or answer[-1] == " ":
                answer += i.upper()
            else:
                answer += i.lower()
        
    return answer
