def solution(ingredient):
    hamburger = []
    result = 0
    
    for i in ingredient:
        hamburger.append(i)
        if hamburger[-4:] == [1, 2, 3, 1]:
            result += 1
            for j in range(4):
                hamburger.pop() 
    return result
            
