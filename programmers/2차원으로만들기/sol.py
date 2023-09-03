def solution(num_list, n):
    answer = []
    result = []
    count = 0
    for i in num_list:
        result.append(i)
        count += 1
        if count == n:
            answer.append(result)
            result = []
            count = 0
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8],2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948],3))