from collections import deque

N, M, V = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True 

visited_bfs = [False]*(N+1)
visited_dfs = [False]*(N+1)

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited_bfs[start_node] = True
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for i in range(1, N+1):
            if not visited_bfs[i] and graph[current][i]:
                queue.append(i)
                visited_bfs[i] = True

def dfs(start_node):
    visited_dfs[start_node] = True
    print(start_node, end=" ")
    for i in range(1, N+1):
        if not visited_dfs[i] and graph[start_node][i]:
            dfs(i)

dfs(V)
print()
bfs(V)
