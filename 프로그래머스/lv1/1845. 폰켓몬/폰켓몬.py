def solution(nums):
    nums_set = set(nums)
    pocket = []
    for i in nums_set:
        if len(pocket) < (len(nums)/2):
            pocket.append(i)
    return len(pocket)