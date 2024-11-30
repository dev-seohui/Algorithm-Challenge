def solution(N, stages):
    arrival = [0] * (N + 2)  

    for stage in stages:
        arrival[stage] += 1

    result = []
    total_players = len(stages) 

    for i in range(1, N + 1):
        if total_players > 0: 
            failure_rate = arrival[i] / total_players
            result.append([i, failure_rate])
            total_players -= arrival[i]  
        else:  
            result.append([i, 0])

    answer = sorted(result, key=lambda x: (-x[1], x[0]))
    return [x[0] for x in answer]
