from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    deque_people = deque(people)
    
    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return answer + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        answer += 1
    return answer
