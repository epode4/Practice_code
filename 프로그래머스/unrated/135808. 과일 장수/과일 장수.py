# k = 사과 최대 점수 m = 상자에 들어가는 사과 수 score = 사과들 점수
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    # 남아있는 사과가 한 상자에 들어가는 개수는 될때까지만
    # while len(score) >= m:
    #     box = score[:m:]
    #     del score[:m:]
    #     answer += box[-1]*m
    # print(score)
    for i in score[m-1::m]:
         answer += i*m
        
    return answer