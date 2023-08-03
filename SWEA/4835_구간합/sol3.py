import sys
sys.stdin = open('input.txt')
from pprint import pprint

t = int(input())

for tc in range(1,t+1):
    # n : 정수의 개수, m : 구간의 개수
    n, m = map(int,input().split())
    numbers = list(map(int,input().split()))

    
    min_number = 1000000
    max_number = 0

    for i in range(n-m+1):
        total = 0
        for j in range(m):
            total += numbers[i+j]

        if total < min_number:
            min_number = total

        if total > max_number:
            max_number = total

    result = max_number - min_number
    print(f'#{tc} {result}')

        