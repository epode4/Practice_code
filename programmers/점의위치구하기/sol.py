def solution(dot):
    answer = 1
    if dot[0] < 0:
        answer +=1
        if dot[1] < 0:
            answer +=1
    elif dot[1] < 0:
        answer += 3
    return answer

print(solution([2,4]))
print(solution([-7,9]))
print(solution([-7,-9]))
print(solution([7,-9]))