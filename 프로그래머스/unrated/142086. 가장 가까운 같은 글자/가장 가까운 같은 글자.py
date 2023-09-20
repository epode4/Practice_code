def solution(s):
    answer = []
    stack = []
    for text in s:
        if text not in stack:
            answer.append(-1)
            stack.append(text)
        else:
            count = 1
            for i in stack[::-1]:
                if i != text:
                    count += 1
                else:
                    break
            answer.append(count)
            stack.append(text)
    return answer