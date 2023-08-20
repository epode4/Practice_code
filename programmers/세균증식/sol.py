def solution(n, t):
    for i in range(t):
        n *= 2
    return n

print(solution(2,10))
print(solution(7,15))