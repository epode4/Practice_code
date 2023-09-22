def solution(s):
    answer = []
    stack = []
    for text in s:
        if text not in stack:
            stack.append(text)
            answer.append(-1)
        else:            
            count = 1
            for i in stack[::-1]:
                if i != text:
                    count += 1
                else:
                    break
            answer.append(count)
            stack.append(text)
            # num_list = [idx for idx, t in enumerate(stack) if t == text]
            # answer.append(num_list[-1]-num_list[-2])

    return answer
