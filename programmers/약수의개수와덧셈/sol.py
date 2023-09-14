def solution(left, right):
    answer = 0
    for i in range(left,right+1):  
        count = []
        for j in range(1,i+1):
            if i % j == 0:
                count.append(j)
        if len(count)%2:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13,17))
print(solution(24,27))