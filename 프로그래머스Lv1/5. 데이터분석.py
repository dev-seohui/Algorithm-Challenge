def solution(data, ext, val_ext, sort_by):
    cols = ['code','date','maximum','remain']
    answer = []
    
    for d in data:
        if d[cols.index(ext)] < val_ext:
            answer.append(d)
    answer = sorted(answer, key=lambda x: x[cols.index(sort_by)])
    return answer
            
