def solution(k, score):
    answer = []
    score_stack = []
    for i in score:
        score_stack.append(i)
        score_stack = sorted(score_stack,reverse=True)[:k]
            
        answer.append(min(score_stack))
            
        
    return answer