# def solution(n):
#     if n <= 1:
#         return 1
#     elif n >= 2:
#         return n * solution(n-1)

# print(solution(5))

def solution(n):
    count = 1
    while n // count != 0:
        print(n,count)
        n = n // count
        count += 1
    return count-1

print(solution(7))
print(solution(3628800))
