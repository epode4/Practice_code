def solution(lottos, win_nums):
    answer = []
    correct = []
    unknown = 0
    my_lotto = [0]*46
    lotto_num = [0]*46
    
    for i in lottos:
        my_lotto[i] += 1
        if i == 0:
            unknown += 1
    for i in win_nums:
        lotto_num[i] += 1
    
    for i in range(45,-1,-1):
        if my_lotto[i] == lotto_num[i] and my_lotto[i] != 0:
            correct.append(i)
    
    
    answer.append(7-(len(correct)+unknown))
    answer.append(7-len(correct))
    
    if answer[-1] == 7:
        answer[-1] = 6
    if answer[0] == 7:
        answer[0] =6
        
    return answer