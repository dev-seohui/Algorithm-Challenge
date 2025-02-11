n = int(input())
num = list(map(int, input().split()))

num.sort()
target = 1

for x in num:
    if x > target:
        break
    target += x 

print(target)
