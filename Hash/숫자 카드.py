import sys

n = int(input())
num1 = list(map(int, sys.stdin.readline().split()))

m = int(input())
num2 = list(map(int, sys.stdin.readline().split()))

dic = {}
for num in num2:
    dic[num] = 0

for num in num1:
    if num in dic:
        dic[num] = 1

answer = [str(value) for key, value in dic.items()]
print(' '.join(answer))
