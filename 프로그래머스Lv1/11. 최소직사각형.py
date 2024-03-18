def solution(sizes):
    w = []
    h = []
    for s in sizes:
        s.sort()
        w.append(s[0])
        h.append(s[1])
    return max(w)*max(h)
