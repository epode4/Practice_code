def solution(numbers):
    answer = 0
    minus = []
    numbers = sorted(numbers)
    for i in numbers:
        if i <0:
            minus.append(i)
    answer = numbers[-1]*numbers[-2]
    if len(minus) >= 2:
        if minus[0]*minus[1] > answer:
            answer = minus[0]*minus[1]
    return answer

print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))