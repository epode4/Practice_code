def solution(a, b, n):
    answer = 0

    while n >= a:
        print(n)
        new, rest = divmod(n,a)
        answer += new*b
        n = rest + new*b

    return answer