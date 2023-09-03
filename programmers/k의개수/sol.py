def solution(i, j, k):
    answer = 0
    for i in range(i,j+1):
        for j in str(i):
            if k == int(j):
                answer += 1
    return answer

print(solution(1,13,1))
print(solution(10,50,5))
print(solution(3,10,2))