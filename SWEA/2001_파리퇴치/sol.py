import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # n : 전체 보드의 길이
    # m : 파리채의 길기
    n, m = list(map(int, input().split()))

    matrix = []

    for _ in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)

    # pprint(matrix)
    total = 0

    # 파리채를 그리기 위한 기준점을 잡기 위한 반복문
    for i in range(n-m+1):
        for j in range(n-m+1):
        #    print(matrix[i][j])
            temp_total = 0

            for row in range(m):
                for col in range(m):
                    temp_total += matrix[i+row][j+col]

            if total < temp_total:
                total = temp_total

    print(total)