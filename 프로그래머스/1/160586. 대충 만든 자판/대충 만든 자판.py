def solution(keymap, targets):
    answer = []
    for target in targets:
        result = 0
        for i in target:
            each_count = []
            for key in keymap:
                if i in key:
                    # print('target = ',target, 'i =',i,'index = ',key.index(i))
                    each_count.append(key.index(i))
                    # print('count = ',each_count)
            # print(each_count)
            if each_count and result != -1:  
                result += (min(each_count) + 1)
            else:
                result = -1
        answer.append(result)
    return answer

