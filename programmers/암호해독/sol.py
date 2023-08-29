# def solution(cipher, code):
#     answer = ''
#     a=0
#     for i in cipher:
#         a += 1
#         if not a % code :
#             answer += i
#     return answer

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

print(solution("dfjardstddetckdaccccdegk",4))