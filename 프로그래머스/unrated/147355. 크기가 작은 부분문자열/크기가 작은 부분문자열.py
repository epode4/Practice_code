def solution(t, p):
    count = 0
    # t에서 -p+1 만큼까지만 돌리기
    # for 문 돌려서 시작점에서 p만큼만 answer에 쌓기
    # p만큼 돈 후 answer 값 p값과 비교
    
    for i in range((len(t)-len(p))+1):
        answer = '' 
        for j in range(len(p)):
            # print(t[i+j])
            answer += t[i+j]
        # print(answer)
        if int(answer) <= int(p):
            count += 1
    return count
