def solution(number, limit, power):
    answer = 0
    # 기사 약수 list 구하기
    for i in range(1,number+1):
        count = 0
        for j in range(1,int(i**(1/2))+1):
            if j**2 == i:
                count += 1
            elif i%j == 0:
                count += 2
        if count > limit:
            count = power
        answer += count
        
    return answer