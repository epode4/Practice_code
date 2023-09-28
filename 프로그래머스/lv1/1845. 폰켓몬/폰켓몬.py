# def solution(nums):
#     pocket = []
#     num = len(nums)/2
#     # print(num)
#     while nums and len(pocket) < num:
#         for i in nums:
#             if i not in pocket:
#                 pocket.append(i)
#                 nums.remove(i)
#             else:
#                 nums.remove(i)
#     return len(pocket)

def solution(nums):
    nums_2 = set(nums)
    pocket = []
    # print(num)
    for i in nums_2:
        if len(pocket) < (len(nums)/2):
            pocket.append(i)
        # print(pocket)
    return len(pocket)