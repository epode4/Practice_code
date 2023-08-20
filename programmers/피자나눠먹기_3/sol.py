def solution(slice, n):
    if slice < n:
        n, m = divmod(n,slice)
        if m:
            n+=1
    else:
        n = 1
    return n

print(solution(7,10))
print(solution(4,12))
print(solution(4,13))