import sys
from collections import deque

left_stack = deque(sys.stdin.readline().strip())
right_stack = deque()
num = int(sys.stdin.readline().strip())
cursor = len(left_stack)

for _ in range(num):   
    cond = sys.stdin.readline().strip()

    if cond[0] == 'L' and left_stack:
        right_stack.appendleft(left_stack.pop())
    elif cond[0] == 'D' and right_stack:
        left_stack.append(right_stack.popleft())
    elif cond[0] == 'B' and left_stack:
        left_stack.pop()
    elif cond[0] == 'P':
        left_stack.append(cond.split()[1])

print("".join(left_stack) + "".join(right_stack))
