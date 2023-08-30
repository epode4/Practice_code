def solution(n, numlist):
    answer = []
    for i in numlist:
        if not i % int(n):
            answer.append(i)
    return answer

print(solution('3',[4, 5, 6, 7, 8, 9, 10, 11, 12]))