import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append((*coins[0], *coins[1], 0))
    visited = set()
    visited.add((*coins[0], *coins[1]))

    while queue:
        x1, y1, x2, y2, count = queue.popleft()

        if count >= 10:
            return -1
        
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and board[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if 0 <= nx2 < n and 0 <= ny2 < m and board[nx2][ny2] == '#':
                nx2, ny2 = x2, y2 

            out1 = not (0 <= nx1 < n and 0 <= ny1 < m)
            out2 = not (0 <= nx2 < n and 0 <= ny2 < m)

            if out1 and out2:
                continue
            if out1 or out2:
                return count + 1
            
            if (nx1, ny1, nx2, ny2) not in visited:
                visited.add((nx1, ny1, nx2, ny2))
                queue.append((nx1, ny1, nx2, ny2, count + 1))
                
    return -1

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

coins = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coins.append((i, j))

print(bfs())
