import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = (map(int, sys.stdin.readline().split()))
max_value, min_value = -10**9, 10**9

def backtrack(index, current_result, add, sub, mul, div):
    global max_value, min_value

    if index == n:
        max_value = max(max_value, current_result)
        min_value = min(min_value, current_result)
        return 
    if add > 0:
        backtrack(index+1, current_result+num[index], add-1, sub, mul, div)
    if sub > 0:
        backtrack(index+1, current_result-num[index], add, sub-1, mul, div)
    if mul > 0:
        backtrack(index+1, current_result*num[index], add, sub, mul-1, div)
    if div > 0:
        if current_result < 0:
            backtrack(index+1, -(-current_result//num[index]), add, sub, mul, div-1)
        else:
            backtrack(index+1, current_result//num[index], add, sub, mul, div-1)    

backtrack(1, num[0], add, sub, mul, div)

print(max_value)
print(min_value)
