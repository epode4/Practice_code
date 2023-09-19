import string

def solution(s, n):
    answer = ''
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    # print(lower,upper)

    for text in s:
        if text == ' ':
            answer += ' '
        if text.isupper():
            idx = upper.index(text)
            answer += upper[(idx+n)%26]
            # s = s.replace(text,upper[idx+n])

        elif text.islower():
            idx = lower.index(text)
            answer += lower[(idx+n)%26]
            # s = s.replace(text,lower[idx+n])

    return answer