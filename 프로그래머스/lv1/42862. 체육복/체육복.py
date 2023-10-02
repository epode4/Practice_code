def solution(n, lost, reserve):
    
    result = [0]*n
    
    for i in lost:
        result[i-1] -= 1
    for i in reserve:
        result[i-1] += 1
    
    # print(result)
    
    if result[0] == -1 and result[1] == 1:
        result[0] += 1
        result[1] -= 1
    if result[-1] == -1 and result[-2] == 1:
        result[-1] += 1
        result[-2] -= 1
    if result[0] == 1 and result[1] == -1:
        result[0] -= 1
        result[1] += 1
     
    # print(result)
        
    for i in range(1, len(result)-1):
        if result[i] == -1 and result[i+1] == 1:
            result[i] += 1
            result[i+1] -= 1
        if result[i] == 1 and result[i+1] == -1:
            result[i] -= 1
            result[i+1] += 1          
        
    
    
    # print(result)
    
    return len(list(x for x in result if x >= 0))
    
# def solution(n, lost, reserve):
    
#     lost.sort()
#     reserve.sort()
    
#     not_lost = []
    
#     for i in range(n):
#         if i+1 not in lost:
#             not_lost.append(i+1)        
    
#     result = []
#     for i in lost:
#         for j in reserve:
#             if i == j:
#                 break
#             if i + 1 == j:
#                 result.append(i)
#                 result.append(j)
                
#     return len(set(not_lost+result))