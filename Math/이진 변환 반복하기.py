def solution(s):
    
    count = 0
    removed_zero = 0
    
    if s == '1':
        return [0, 0]
    
    length = len(s.replace("0", ""))
    binary = bin(length)[2:]
    removed_zero += (len(s) - length)
    count += 1
    
    new_count, new_removed_zero = solution(binary)
    
    return [count+new_count, removed_zero+new_removed_zero]
