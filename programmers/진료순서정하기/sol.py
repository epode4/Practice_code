def solution(emergency):
    answer = []
    sort_dict = {}
    sort_a = (emergency.copy())
    sort_a.sort(reverse=True)
    # print(sort_a)
    for i in sort_a:
        sort_dict[i] = sort_a.index(i)+1
    # print(sort_dict)

    for i in emergency:
        answer.append(sort_dict[i])

    return answer

print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))