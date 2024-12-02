def solution(prices):
    n = len(prices)
    answer = [0]*n
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = n - idx - 1
    return answer
