def solution(money):
    answer = list(divmod(money, 5500))

    return answer

print(solution(5500))
print(solution(15000))