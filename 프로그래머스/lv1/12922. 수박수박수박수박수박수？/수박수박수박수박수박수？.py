def solution(n):
    answer = ''
    watermelon = ['수', '박'] # 0,1,0,1
    for i in range(n): 
        answer += watermelon[i%2] 
    return answer