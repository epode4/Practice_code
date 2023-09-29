def solution(dartResult):
    result = []
    for idx, i in enumerate(dartResult):
        if i.isdigit() and i != '0':
            result.append(int(i))
        elif i == '0' and dartResult[idx-1] == '1':
            result[-1]=10
        elif i == '0':
            result.append(int(i))
            
        else:
            if i=='S':
                result[-1] = result[-1]**1
            elif i=='D':
                result[-1] = result[-1]**2
            elif i=='T':
                result[-1] = result[-1]**3
            elif i == '*':
                if len(result) >= 2:
                    result[-1], result[-2] = result[-1]*2, result[-2]*2
                else:
                    result[-1] = result[-1]*2
            elif i== '#':
                result[-1] = result[-1]*-1
                
        # print(result)
    return sum(result)