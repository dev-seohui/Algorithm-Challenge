def solution(keymap, targets):
    answer = []
    
    for target in targets:
        counts = 0
        for t in target:
            found = False
            count = 101
            for key in keymap:
                if t in key:
                    count = min(key.index(t)+1, count)
                    found = True
            if not found:
                counts = -1
                break
            counts += count 
        answer.append(counts)
    return answer
