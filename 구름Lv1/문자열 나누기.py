N = int(input())
S = str(input())
stack = []
answer = 0

for alphabet in S:
	if not stack:
		stack.append(alphabet)
	elif stack[-1] != alphabet:
		answer += 1
		stack = [alphabet]
if stack:
	answer += 1
print(answer)
