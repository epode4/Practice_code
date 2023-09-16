def solution(a, b):
    answer = 0
    for p, q in zip(a,b):
        answer += p*q
    return answer