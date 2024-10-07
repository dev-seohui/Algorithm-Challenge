def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            else:
                stack.pop()    
    while stack:
        return False

    return True
