def solution(sizes):
    bigger = max(sizes[0][0], sizes[0][1])
    smaller = min(sizes[0][0], sizes[0][1])

    for i in range(1, len(sizes)):
        if max(sizes[i][0], sizes[i][1]) > bigger:
            bigger = max(sizes[i][0], sizes[i][1])
        if min(sizes[i][0], sizes[i][1]) > smaller:
            smaller = min(sizes[i][0], sizes[i][1])

    return bigger*smaller
