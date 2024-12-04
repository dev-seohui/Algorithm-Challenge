import sys
input = sys.stdin.readline

def solution(x, y, n):
    global white, blue
    color = paper[x][y]
    for row in range(x, x+n):
        for col in range(y, y+n):
            if color != paper[row][col]:
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return 
    if color == 0:
        white += 1
    else:
        blue += 1

white, blue = 0, 0
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

solution(0, 0, n)
print(white)
print(blue)
