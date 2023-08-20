def solution(n):
    answer = 1
    if (n **(1/2))%1 :
        answer = 2
    return answer

print(solution(144))
print(solution(976))