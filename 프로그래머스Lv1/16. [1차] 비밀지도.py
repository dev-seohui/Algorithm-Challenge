def solution(n, arr1, arr2):
    answer = []

    nrr1 = [f'{x:0{n}b}' for x in arr1]
    nrr2 = [f'{x:0{n}b}' for x in arr2]

    for i in range(n):
        temp = ""
        for j in range(n):
            if nrr1[i][j] == '1' or nrr2[i][j] == '1':
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer
