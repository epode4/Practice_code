def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i) * (food[i]//2)
    
    answer_reverse = answer[::-1]
    answer = answer + '0' + answer_reverse

    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))