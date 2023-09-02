def solution(num, k):
    answer = -1
    count = 0
    for i in str(num):
        count += 1
        if i == str(k):
            return count
    return answer

print(solution(29183,1))
print(solution(232443,4))
print(solution(123456,7))