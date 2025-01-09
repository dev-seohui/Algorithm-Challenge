import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for neighbor in adjacent_list[node]:
        if not visited[neighbor]:
            dfs(neighbor)

n, m = map(int, input().split())
adjacent_list = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adjacent_list[u].append(v)
    adjacent_list[v].append(u)

visited = [False] * (n + 1)
components = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        components += 1

print(components)
