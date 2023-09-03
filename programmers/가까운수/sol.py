def solution(array, n):
    min_num = 100000000
    for i in array:
        if abs(n-i) < min_num:
            min_num = abs(n-i)
            result = i
        elif abs(n-i) == min_num:
            if result > i:
                result = i
    return result

print(solution([3,10,28], 20))
print(solution([10,11,12], 13))