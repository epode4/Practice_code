import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    min_number = 1000000
    max_number = 0

    for i in numbers:
        if min_number > i:
            min_number = i

        if max_number < i:
            max_number = i
    result = max_number - min_number

    print(f'#{tc} {result}')

