def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

print(solution([149,180,192,170],167))