from collections import deque

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            adjacency_list[b].append(a)
            in_degree[a] += 1 

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        takenCourses = 0

        while queue:
            course = queue.popleft()
            takenCourses += 1

            for neighbor in adjacency_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return takenCourses == numCourses
