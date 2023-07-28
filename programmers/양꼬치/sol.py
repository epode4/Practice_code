# n => 양꼬치 n인분
# k => 음료수 k개


def solution(n, k):
    k = k - (n//10)
    answer = n * 12000 + k * 2000
    return answer

print(solution(10,3))
print(solution(64,6))