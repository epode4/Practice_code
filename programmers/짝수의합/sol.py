def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 ==0:
            answer += i
    return answer

print(solution(10))
print(solution(4))

# 2.

# def solution(n):
#     answer = []

#     for i in range(n+1):
#         if i % 2 == 0:
#             answer.append(i)

#     return sum(answer)

# 3. 

# def solution(n):

#     answer = range(0, n+1, 2)

#     return sum(answer)