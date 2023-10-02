def solution(n, lost, reserve):
    
    result = [0]*n
    
    for i in lost:
        result[i-1] -= 1
    for i in reserve:
        result[i-1] += 1
    
    # 맨 앞 2 케이스만 따로 계산
    if result[0] == -1 and result[1] == 1:
        result[0] += 1
        result[1] -= 1
        
    if result[0] == 1 and result[1] == -1:
        result[0] -= 1
        result[1] += 1

    # 나머지 index 1부터 마지막 전까지 다음 것과 비교
    for i in range(1, len(result)-1):
        if result[i] == -1 and result[i+1] == 1:
            result[i] += 1
            result[i+1] -= 1
        if result[i] == 1 and result[i+1] == -1:
            result[i] -= 1
            result[i+1] += 1          
        
    
    return len(list(x for x in result if x >= 0))
    