def solution(my_string, n):
    answer = []
    for i in my_string:
        answer.append(i*n)
    answer = ''.join(answer)

    return answer


print(solution('hello',3))