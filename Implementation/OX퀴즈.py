
n = int(input())

for _ in range(n):
    answer = []
    prev = ""
    ox = str(input())

    for current in ox:
        if current != "X":
            if prev != "X":
                add = answer[-1]+1 if answer else 1
                answer.append(add)
            else:
                answer.append(1)
        prev = current 
    print(sum(answer))
