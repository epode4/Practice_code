def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))

    answer = sorted(answer)
    return answer

print(solution("hi12392"))
print(solution("abcde0"))