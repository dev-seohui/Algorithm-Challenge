from collections import deque

def bfs(adjacent_list, start_node):
    count = 0
    visited = []
    queue = deque([start_node])
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            count += 1
            queue.extend(adjacent_list[current])
    return count -1

n = int(input())
e = int(input())

adjacent_list = {i:[] for i in range(1, n+1)}

for _ in range(e):
    x, y = map(int, input().split())
    adjacent_list[x].append(y)
    adjacent_list[y].append(x)

bfs_result = bfs(adjacent_list, 1)
print(bfs_result)
