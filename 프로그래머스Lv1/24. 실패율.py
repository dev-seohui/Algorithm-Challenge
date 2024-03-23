def solution(N, stages):
    T = len(stages)
    F = []

    for s in range(1, N+1):
        U = stages.count(s)
        if T == 0:
            rate = 0
        else:
            rate = U / T
        F.append((s, rate))
        T -= U

    F.sort(key=lambda x: (-x[1], x[0]))
    return [s for s, _ in F]
