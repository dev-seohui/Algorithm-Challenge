
def solution(s):
    
    stack = []
    i = 0
    
    while i < len(s):
        if not stack or (stack[-1] != s[i]):
            stack.append(s[i])
        else:
            stack.pop()
        i += 1
    
    if not stack:
        return 1
    else:
        return 0
        
            
