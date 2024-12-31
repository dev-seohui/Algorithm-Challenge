
n = int(input())
answer = 0

for _ in range(n):
    word = str(input())
    seen = set()
    prev = ""
    is_group = True

    for current in word:
        if current != prev:
            if current in seen:
                is_group = False
            seen.add(current)
        prev = current 
    
    if is_group:
        answer += 1
    
print(answer)
