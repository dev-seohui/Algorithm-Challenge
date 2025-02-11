import sys
import itertools

while True:
    num = sys.stdin.readline().strip()
    if num == '0':
        break
    num_list = list(num.split())[1:]
    num_list = list(map(int, num_list))
    # num_list.sort()
    
    results = list(itertools.combinations(num_list, 6))
    for result in results:
        print(" ".join(map(str, result)))
    print()
