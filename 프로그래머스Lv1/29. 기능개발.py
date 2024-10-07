def solution(progresses, speeds):
    answer = []
    days = []
    stack = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] != 0:
            days.append((100-progresses[i])//speeds[i]+1)
        else:
            days.append((100-progresses[i])//speeds[i])
    print(days)

    first_day = days[0]
    count = 1

    for i in range(1, len(days)):
        if days[i] <= first_day:        
            count += 1
        else:
            answer.append(count)
            first_day = days[i]
            count = 1
    answer.append(count)
    return answer
