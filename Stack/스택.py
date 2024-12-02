import sys
n = int(sys.stdin.readline())

stack = []
for case in range(n):
  lst = sys.stdin.readline().split()
  if lst[0] == "push":
    stack.append(int(lst[1]))
  elif lst[0] == "pop":
    print(int(stack.pop()) if stack else -1)
  elif lst[0] == "size":
    print(len(stack))
  elif lst[0] == "empty":
    print(1 if not stack else 0)
  elif lst[0] == "top":
    print(stack[-1] if stack else -1)

"""
입력받을 때 입출력 속도에 따라 런타임 에러가 뜬다.
한 줄을 받을 때는 input을 사용해도 되지만, 반복문을 통해 입력받을 때는 주의
"""
