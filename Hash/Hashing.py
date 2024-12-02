n = int(input())
word = str(input())
m = 1234567891
# a->1, ..., z->26 (문제)
# a->97, ..., z->122 (아스키)

answer = 0
for i in range(n):
  num = ord(word[i]) - 96
  answer += num*(31**i)
print(answer%m)
