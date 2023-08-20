def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

# 중복값은 안 되는 set 성질 이용하는 코드
def solution(s1, s2):
    return len(set(s1)&set(s2))

print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"],["m", "dot"]))