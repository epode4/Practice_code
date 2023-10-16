def solution(s):
    answer = 0
    x = s[0]
    count_s = 0
    count_d = 0
    for i in range(len(s)-1):
        print('x =',x, 'i =',s[i])
        if s[i] == x:
            count_s += 1
        else: 
            count_d += 1
        if count_s == count_d:
            answer += 1
            x = s[i+1]
    return answer+1