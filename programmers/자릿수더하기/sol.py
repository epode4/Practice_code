def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer


# def solution(n):
#     answer = sum(list(map(int,str(n))))
#     return answer


# def solution(n):
#     answer = 0
#     while n > 0:
#         a, b = divmod(n,10)
#         n = a
#         answer += b

#     return answer


print(solution(1234))
print(solution(930211))
