def solution(num1, num2):
    if num1 == num2:
        return 1
    elif num1 != num2:
        return -1

print(solution(2,3))
print(solution(11,11))
print(solution(7,99))