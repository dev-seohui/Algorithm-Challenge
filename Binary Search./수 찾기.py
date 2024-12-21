import sys

n = int(input())
arr1 = list(set(map(int, sys.stdin.readline().split())))
arr1.sort()

m = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

def binary_search(target, data):
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start + end)//2
        if data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
        else:
            return 1
    return 0

for num in arr2:
    if binary_search(num, arr1):
        print(1)
    else:
        print(0) 
