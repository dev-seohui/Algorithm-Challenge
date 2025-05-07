from collections import deque

def solution(l, r):
    
    answer = []
    queue = deque(['5'])
    
    while queue:
        num_str = queue.popleft()
        num = int(num_str)
        
        if num > r:
            continue
        if num >= l:
            answer.append(num)
            
        queue.append(num_str + '0')
        queue.append(num_str + '5')
            
    return sorted(answer) if answer else [-1]
