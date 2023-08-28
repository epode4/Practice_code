def solution(hp):
    ant = [5,3,1]
    answer = 0

    for i in ant:
        count, hp = divmod(hp,i)
        answer += count   
    return answer

print(solution(23))
print(solution(24))
print(solution(999))