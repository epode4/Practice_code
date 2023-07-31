def solution(n):
    n = str(n)
    answer = 0
    for i in n:
        answer += int(i)
    return answer


# def solution(n):
#     answer = sum(list(map(int,str(n))))
#     return answer

print(solution(1234))
print(solution(930211))
