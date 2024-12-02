def solution(phone_book):
    
    dic = {}
    
    for num in phone_book:
        dic[num] = True
        
    for num in phone_book:
        prefix = ""
        for n in num:
            prefix += n
            if prefix in dic and prefix != num:
                return False
    return True
