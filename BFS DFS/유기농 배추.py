from collections import deque

def bfs(i, j, m, n, field):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(i, j)])
    field[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and field[nx][ny]==1:
                field[nx][ny] = 0
                queue.append((nx, ny))
            

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j, m, n, field)
                count += 1
    print(count)
                

