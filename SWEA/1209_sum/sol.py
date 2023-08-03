import sys
sys.stdin = open('input.txt')

t = 10

for tc in range(1,t+1):
    tc = int(input())

    matrix = []
    row_max = 0
    col_max = 0
    dia_max1 = 0
    dia_max2 = 0

    for i in range(100):
        numbers = list(map(int,input().split()))
        matrix.append(numbers)

    for r in range(len(matrix)):
        sum_r = 0
        for c in range(len(matrix[0])):
            sum_r += (matrix[r][c])
        if sum_r > row_max:
            row_max = sum_r

    for c in range(len(matrix[0])):
        sum_c = 0
        for r in range(len(matrix)):
            sum_c += (matrix[r][c])
        if sum_c > col_max:
            col_max = sum_c

    sum_x = 0

    for r in range(len(matrix)):
        dia_max1 += matrix[r][r]

    for r in range(1, len(matrix)):
        dia_max2 += matrix[r][-r]

    print(row_max, col_max, dia_max1, dia_max2)

    result = max(row_max,col_max,dia_max1,dia_max2)
    # print(f'#{tc} {result}')