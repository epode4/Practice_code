def solution(d, budget):
    # 반복문 돌아서 count(len) 한 뒤에 더 많은 수가 들어올 때 바꾸기
    # budget에서 d의 요소들 최소부터 빼기
    d.sort()
    count = []
    for i in d:
        if (budget-i) >= 0:
            budget -= i
            count.append(i)
    return len(count)

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))