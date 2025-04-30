from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))
    count = 0

    while queue:
        idx, current_sum = queue.popleft()

        if idx == len(numbers):
            if current_sum == target:
                count += 1
        else: 
            queue.append((idx+1, current_sum+numbers[idx]))
            queue.append((idx+1, current_sum-numbers[idx]))

    return count
