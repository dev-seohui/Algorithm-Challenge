def solution(k, score):
    top_k = []
    result = []
    for i in range(len(score)):
        if len(top_k)<k:
            top_k.append(score[i])
        else:
            min_k = min(top_k)
            if min_k <= score[i]:
                top_k.remove(min_k)
                top_k.append(score[i])
        result.append(min(top_k))
    return result
