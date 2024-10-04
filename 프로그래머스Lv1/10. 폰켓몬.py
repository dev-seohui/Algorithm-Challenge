def solution(nums):
    list_len = (len(nums))//2
    set_nums = set(nums)
    set_len = len(set_nums)
    # print(list_len, set_len)
    return min(list_len, set_len)
