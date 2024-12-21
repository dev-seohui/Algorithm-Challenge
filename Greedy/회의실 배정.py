import sys

n = int(input())
meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings = sorted(meetings, key=lambda x:(x[1], x[0]))

time = 0
answer = 0

for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        answer += 1

print(answer)
