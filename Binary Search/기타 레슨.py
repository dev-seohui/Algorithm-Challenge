
n, m = map(int, input().split())
num = list(map(int, input().split()))

def check(mid):
    count = 1
    total = 0
    for current in num:
        if total + current > mid:
            count += 1
            total = current
        else:
            total += current
    return count 

def binary_search(n, m):
    start = max(num)
    end = sum(num)
    result = end 

    while start <= end:
        mid = (start+end)//2
        if check(mid) <= m:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result 

print(binary_search(n, m))
