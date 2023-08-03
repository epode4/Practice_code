import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1,t+1):
    # n : 배열 길이 / m : 파리채 길이
    n, m = map(int,input().split())
    matrix = []

    for i in range(n):
        matrix.append(list(map(int,input().split())))

    total = 0

    for row in range(n-m+1):
        for col in range(n-m+1):
            sum = 0

            for i in range(m):
                for j in range(m):
                    sum += matrix[row+i][col+j]

            if total < sum:
                total = sum

    print(f'#{tc} {total}')