import itertools

n, s = map(int, input().split())
num = list(map(int, input().split()))

all_combinations = []
for i in range(len(num)):
    all_combinations.extend(itertools.combinations(num, i+1))

result = 0
for comb in all_combinations:
    if sum(comb) == s:
        result += 1
print(result)
