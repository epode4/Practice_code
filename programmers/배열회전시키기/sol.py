def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0,numbers.pop(-1))
    else:
        numbers.append(numbers.pop(0))
    return numbers

print(solution([1,2,3],'right'))
print(solution([4, 455, 6, 4, -1, 45, 6],'left'))