def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = []
        dic[genres[i]].append((i, plays[i]))
    
# Ex : {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
    total = {}
    for d in dic:
        total[d] = sum([x[1] for x in dic[d]])
    total = sorted(total.items(), key=lambda x:x[1], reverse=True)
# Ex : 	[('pop', 3100), ('classic', 1450)]
    
    answer = []
    for j, _ in total:
        songs = sorted(dic[j], key=lambda x:x[1], reverse=True)
        for k in range(min(2, len(songs))):
            answer.append(songs[k][0])
    return answer
