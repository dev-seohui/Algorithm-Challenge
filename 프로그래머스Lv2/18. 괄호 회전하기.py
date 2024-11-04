
def solution(s):
    answer = 0
    for k in range(len(s)):
        new_s = s[k:] + s[:k]
        stack = []
        is_valid = True
        for i in new_s:
            if i in "[{(":
                stack.append(i)
            elif i == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif i == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                is_valid = False
                break
        if is_valid and not stack:
            answer += 1
    return answer
