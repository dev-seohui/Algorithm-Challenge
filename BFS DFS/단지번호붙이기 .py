from collections import deque

def bfs(x, y, n, maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    maps[x][y] = 0
    count = 1 

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<n and maps[nx][ny]==1:
                maps[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count 

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]

complex_counts = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            complex_counts.append((bfs(i, j, n, maps)))

complex_counts.sort()
print(len(complex_counts))
for count in complex_counts:
    print(count)
