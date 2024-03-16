def solution(nums):
    list_len = (len(nums)+1)//2
    set_nums = set(nums)
    set_len = len(set_nums)
    # print(list_len, set_len)
    if set_len > list_len:
        return list_len
    else:
        return set_len
