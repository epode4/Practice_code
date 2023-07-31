def solution(num_list):
    return num_list[::-1]


# def solution(num_list):
#     num_list.reverse()
#     return num_list


# def solution(num_list):
#     answer = []    
#     for num in num_list:
#         answer.insert(0,num)

#     return answer


# def solution(num_list):
#     answer = []

#     for i in range(len(num_list)):
#         data = num_list[len(num_list)-i-1]
#         answer.append(data)
#     return answer


print(solution([1,2,3,4,5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))