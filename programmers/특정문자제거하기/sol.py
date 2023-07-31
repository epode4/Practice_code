def solution(my_string, letter):

    for i in my_string:
        if i == letter:
            answer = my_string.replace(i,'')
    return answer

# def solution(my_string, letter):
#     answer = my_string.replace(letter,'')
#     return answer


print(solution('abcdef','f'))
print(solution('BCBdbe','B'))
