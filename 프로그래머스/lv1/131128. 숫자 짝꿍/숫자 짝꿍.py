def solution(X, Y):
    answer = ''
    x_list = [0]*10
    y_list = [0]*10
    
    for x in X:
        x_list[int(x)] += 1
    for y in Y:
        y_list[int(y)] += 1
    
    for i in range(9,-1,-1):
        if x_list[i] < y_list[i]:
            answer += str(i)*(x_list[i])
        else:
            answer += str(i)*(y_list[i])

    if len(answer) == 0:
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
        
    return answer
    
#     return ''.join(nums_list)

# def solution(X, Y):
#     nums_list = []
#     x_list = list(x for x in X)
#     y_list = list(y for y in Y)
    
#     for idx_a, a in enumerate(x_list):
#         for idx_b, b in enumerate(y_list):
#             if a == b:
#                 nums_list.append(a)
#                 x_list[idx_a], y_list[idx_b] = '', ''
#                 break
                
#     nums_list.sort(reverse = True)
    
#     if len(nums_list) == 0:
#         nums_list.append('-1')
#     if nums_list[0] == '0':
#         nums_list = ['0']
    
#     return ''.join(nums_list)