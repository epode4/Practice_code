def solution(my_string):
    m = 'aeiou'
    for i in my_string:
        if i in m:
            my_string = my_string.replace(i,'')
    return my_string

print(solution('bus'))
print(solution('nice to meet you'))