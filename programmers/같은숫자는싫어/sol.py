def solution(arr):
        
    answer = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            # if (answer[-1:]) != arr[i]:
            answer.append(arr[i])

        # elif arr[i] != arr[i-1] and arr[i] != arr[i+1]:
        #     answer.append(arr[i])

    answer.append(arr[-1])
    return answer

    # for i in range(len(arr)-1,0,-1):
    #     if arr[i] == arr[i-1]:
    #         arr.pop(i)
    # return arr



print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
print(solution([2,1,1,3,4]))



# def solution(arr):
        
#     answer = []
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             answer.append(arr[i])
#             if answer[-1:] == answer[-2:-1]:
#                 answer.pop()

#         elif arr[i] != arr[i-1] and arr[i] != arr[i+1]:
#             answer.append(arr[i])
#     return answer