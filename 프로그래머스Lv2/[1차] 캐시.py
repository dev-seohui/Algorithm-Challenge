
from collections import deque   

def solution(cacheSize, cities):
    
    answer = 0
    que = deque()
    
    if cacheSize == 0:
        answer = 5*len(cities)
        return answer
    
    for city in cities:
        city = city.lower()
        
        if len(que) == cacheSize:
            if city in que:
                answer += 1
                que.remove(city)  
                que.append(city)
            else:
                que.popleft()
                que.append(city)
                answer += 5
        else:
            if city in que:
                answer += 1
                que.remove(city)  
                que.append(city)
            else:
                que.append(city)
                answer += 5
                
    return answer
