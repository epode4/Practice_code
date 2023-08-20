def solution(sides):
    mymax = max(sides)
    sides.remove(mymax)
    answer = 2
    if sum(sides) > mymax:
        answer = 1
    return answer

print(solution([1,2,3]))
print(solution([3,6,2]))
print(solution([199,72,222]))