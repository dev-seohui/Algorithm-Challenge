n = int(input())
for case in range(n):
  paren = input()
  stack = []

  for p in paren:
    if p == "(":
      stack.append(p)
    else:
      if not stack:
        print("NO")
        break
      else:
        stack.pop()
  else:
    if stack:
      print("NO")
    else:
      print("YES")

# def로 구현하는 게 아닌 경우에는 for문이 끝나고 else를 적어야 하는 것을 기억하자
