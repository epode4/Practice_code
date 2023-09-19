def solution(array, commands):
    answer = []
    
    for num in commands:
        start = num[0]
        end = num[1]
        idx = num[2]-1

        arr = sorted(array[start-1:end])
        answer.append(arr[idx])
    return answer
