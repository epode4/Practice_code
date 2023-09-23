def solution(nums):
    result = 0
    answer = 0
    for a in range(len(nums)-2):       
        for b in  range(a+1,len(nums)-1):
            for c in  range(b+1,len(nums)):
                result = nums[a] + nums[b] + nums[c]
                if all(result % j != 0 for j in range(2, result)):
                    answer += 1
    return answer