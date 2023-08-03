import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    numbers = list(map(int,input().split()))

    # 정렬 후 큰 수, 작은 수 뽑아서 연산
    # numbers.sort()
    # print(f'#{tc} {numbers[-1]-numbers[0]}')

    # min, max 함수 사용
    # print(f'#{tc} {max(numbers)-min(numbers)}')

    # 버블정렬처럼 다 비교
    min_number = 1000000  # min_number = numbers[0]
    max_number = 0 # max_number = numbers[0]

    for number in numbers:
        if min_number > number:
            min_number = number

        if max_number < number:
            max_number = number

    print(f'#{tc} {max_number-min_number}')
