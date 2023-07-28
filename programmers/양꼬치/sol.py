def solution(n, k):
    k = k - int((n//10))
    answer = n * 12000 + k * 2000
    return answer

print(solution(10,3))
print(solution(64,6))