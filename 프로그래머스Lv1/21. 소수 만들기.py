def solution(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                if num < 2:
                    continue
                is_prime = True
                for x in range(2, int(num ** 0.5) + 1):
                    if num % x == 0:
                        is_prime = False
                        break
                if is_prime:
                    count += 1
    return count
