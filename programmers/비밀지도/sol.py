from pprint import pprint

def solution(n, arr1, arr2):

    # 이진수 배열로 만들기
    list_1 = []
    list_2 = []
    for i in range(n):
        # 이진수 변환 함수
        a = format(arr1[i],'b')
        # 앞에 0으로 들어온 부분 채우기
        if len(a) <n:
            a = (n-len(a))*'0' + a
        list_1.append(list(a))

        b = format(arr2[i],'b')
        if len(b) < n:
            b = (n-len(b))*'0' + b
        list_2.append(list(b))

    # pprint(list_1)
    # pprint(list_2)

    result = []

    for i in range(n):
        result_str = ''
        for j in range(n):
            if list_1[i][j] == '1' or list_2[i][j] == '1':
                result_str += '#'
            else:
                result_str += ' '
        result.append(result_str)

    return result





print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))