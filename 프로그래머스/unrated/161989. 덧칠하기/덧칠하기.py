def solution(n, m, section):
    answer = 0
    while len(section) > 1:
        start = section.pop(0)
        paint = start + m
        answer += 1
        
        # delect = list(x for x in section if x < paint)
        delect = []
        for x in section:
            if x < paint:
                delect.append(x)
            else:
                break
        for y in delect:
            section.remove(y)
            
    if len(section):
        answer += 1
    return answer