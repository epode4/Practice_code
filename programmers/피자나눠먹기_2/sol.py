def solution(n):
    answer = 1
    pizza = 6
    while pizza % n != 0:
        pizza += 6
        answer += 1
    return answer

print(solution(6))
print(solution(10))
print(solution(4))