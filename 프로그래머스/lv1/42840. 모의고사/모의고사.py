def solution(answers):
    one = [1,2,3,4,5] + [1,2,3,4,5]*int(len(answers)/5)
    two = []
    three = []
    for i in [1,3,4,5]:
        two.append(2)
        two.append(i)
        
    two = two + two * int(len(answers)/8)
    
    for i in [3,1,2,4,5]:
        three.append(i)
        three.append(i)
        
    three = three + three * int(len(answers)/10)
        
        
    score = [0,0,0]    
    # print(one, two, three)
    for i, a,b,c in zip(answers,one, two, three):
        if i == a:
            score[0] += 1
        if i == b:
            score[1] += 1
        if i == c:
            score[2] += 1
    
    result = []
    for idx, i in enumerate(score):
        print(i,idx)
        if i == max(score):
            result.append(idx+1)
    # print(result)
    return result