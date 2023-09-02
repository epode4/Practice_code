def solution(order):
    answer = 0
    for i in str(order):
        if i in ('3','6','9'):
            answer += 1
    return answer

print(solution(3))
print(solution(29423))