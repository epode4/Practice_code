def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
    return answer


# def solution(n):
#     answer = 0
#     for i in range(1,int(n**0.5)):
#         if n % i == 0:
#             answer += 2

#             if num * num = n:
#                 answer -= 1
#     return answer

print(solution(20))
print(solution(100))