def solution(age):
    answer = ''
    aList = [chr(i) for i in range(ord('a'),ord('z')+1)]
    # print(aList)
    for i in (str(age)):
        # print(i)
        answer += aList[int(i)]
    return answer

print(solution(23))
print(solution(51))
print(solution(100))