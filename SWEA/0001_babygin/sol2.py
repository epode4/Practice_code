import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    cards = list(map(int,''.join(input())))

    numbers = [ 0 for _ in range(10)]

    for i in cards:
        numbers[i] += 1
    # print(numbers)

    count = 0

    for i in range(len(numbers)):
        if numbers[i] >= 3:
            count += 1
            numbers[i] = 0

    # print(numbers, count)

    for j in range(8):
        if numbers[j] and numbers[j+1] and numbers[j+2]:
            count += 1
            numbers[j] = 0
            numbers[j+1] = 0
            numbers[j+2] = 0

    # print(numbers, count)

    print(cards, count)
