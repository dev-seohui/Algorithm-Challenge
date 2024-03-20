def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        code = ""
        str1, str2 = bin(arr1[i])[2:].zfill(n), bin(arr2[i])[2:].zfill(n)
        # print(str1, str2)
        for j in range(n):
            if str1[j]!='0' or str2[j]!='0':
                code += "#"
            else:
                code += " "
        answer.append(code)
    # print(answer)
    return answer
