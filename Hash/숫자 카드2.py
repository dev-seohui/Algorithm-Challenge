import sys

n = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

dic = {}
for num in arr1:
    if num not in dic:
        dic[num] = 0
    dic[num] += 1

answer = []
for num in arr2:
    answer.append(str(dic[num]) if num in dic else '0')

print(" ".join(answer))
