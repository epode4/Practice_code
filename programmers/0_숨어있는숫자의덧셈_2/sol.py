def solution(my_string):
    answer = 0
    num = '123456789'
    numbers = ''
    for i in range(len(my_string)):
        if my_string[i] in num and my_string[i-1] not in num:
            numbers += my_string[i]
            while my_string[i+1] in num:
                numbers += my_string[i+1]
                i += 1
            answer += int(numbers)
            numbers = ''
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))