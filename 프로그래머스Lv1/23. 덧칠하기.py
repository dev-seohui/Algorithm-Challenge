def solution(n, m, section):
    count = 1
    start = section[0]
    for i in range(1, len(section)):
        if section[i]-start >= m:
            count += 1
            start = section[i]
    return count
