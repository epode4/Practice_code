def solution(arr):
    
    for i in range(len(arr)-1,0,-1):
        if arr[i] == arr[i-1]:
            arr.pop(i)
    return arr

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
