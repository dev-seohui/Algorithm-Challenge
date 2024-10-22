
def solution(s):
    answer = ''
    words = s.split(" ")  

    for w in words:
        word = ""
        for i in range(len(w)):
            if i % 2 == 0:  
                word += w[i].upper() 
            else:  
                word += w[i].lower()  
        answer += word + " "  

    return answer[:-1]  
