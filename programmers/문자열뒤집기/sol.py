def solution(my_string):
    answer = ''
    for i in range(1, len(my_string)+1):
        answer = answer + (my_string[-i])
    return answer

print(solution('jaron'))
print(solution('bread'))


# def solution(my_string):
#     return my_string[::-1]


# print(solution('jaron'))
# print(solution('bread'))
