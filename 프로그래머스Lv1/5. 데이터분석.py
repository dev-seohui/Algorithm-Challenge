def solution(data, ext, val_ext, sort_by):

    lst = ["code", "date", "maximum", "remain"]
    index = lst.index(ext)
    index1 = lst.index(sort_by)
    result = []
    for i in range(len(data)):
        if data[i][index] < val_ext:
            result.append(data[i])

    result.sort(key = lambda x:x[index1])
    return result
