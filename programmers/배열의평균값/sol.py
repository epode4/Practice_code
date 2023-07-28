def solution(numbers):
    start = 0
    for i in numbers:
        start += i
    answer = start/len(numbers)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))