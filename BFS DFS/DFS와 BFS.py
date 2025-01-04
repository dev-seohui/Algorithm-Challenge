from collections import deque

def dfs(adjacent_list, start_node):
    visited = []
    stack = [start_node] 
    while stack:
        current = stack.pop()  
        if current not in visited:
            visited.append(current)  
            stack.extend(reversed(adjacent_list[current]))
    return visited

def bfs(adjacent_list, start_node):
    visited = [] 
    queue = deque([start_node]) 
    while queue:
        current = queue.popleft()  
        if current not in visited:
            visited.append(current) 
            queue.extend(adjacent_list[current])  
    return visited

n, m, v = map(int, input().split())  
adjacent_list = {i: [] for i in range(1, n + 1)}  

for _ in range(m):
    a, b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)

for key in adjacent_list:
    adjacent_list[key].sort()

dfs_result = dfs(adjacent_list, v)
print(" ".join(map(str, dfs_result)))

bfs_result = bfs(adjacent_list, v)
print(" ".join(map(str, bfs_result)))
