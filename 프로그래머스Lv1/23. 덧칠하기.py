
def solution(n, m, section):

    count = 0
    current = 0

    for s in section:
        if s > current:
            count += 1
            current = s+m-1

    return count
