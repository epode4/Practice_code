import sys
sys.stdin =open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int,input().split())
    numbers = list(map(int,input().split()))

    min_total = 100000000
    max_total = 0

    # 구간합을 구하기 위한 i : 뒤의 m개의 데이터를 더하기 위한 시작점
    # index out of range error를 발생시키지 않기 위해
    for i in range(n-m+1):
        
        total = 0
        # 시작점을 기준으로 오른쪽 m개를 구하기위한 반복문
        for j in range(m):
            total += numbers[i+j]
        
        if total < min_total:
            min_total = total

        if total > max_total:
            max_total = total

    result =  max_total - min_total 
    print(f'#{tc} {result}')