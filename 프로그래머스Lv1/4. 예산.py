def solution(d, budget):
    d.sort()
    i = 0
    count = 0

    while i < len(d) and budget >= d[i]:
        budget -= d[i]
        i += 1
        count += 1

    return count
