def solution(N, stages):
    answer = []
    # 각 스테이지별 도전자 수와 실패자 수 구하기
    # range error 피하기 위해 N+1까지
    stage_user = [0]*(N+1)
    stage_fail = [0]*(N+1)
    
    for stage in stages:
        for i in range(stage):
            stage_user[i] += 1
            
        if stage <= N:
            stage_fail[stage-1] += 1
        
    fail_count = []
    for user, fail in zip(stage_user, stage_fail):
        if user==0 or fail==0:
            fail_count.append(0)
        else:
            fail_count.append(fail/user)
    
    while len(answer) < N:
        answer.append(fail_count.index(max(fail_count))+1)
        fail_count[fail_count.index(max(fail_count))] = -1
        
    return answer