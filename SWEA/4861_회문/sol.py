import sys
from pathlib import Path
from pprint import pprint
import math

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n, m = map(int,input().split())
    matrix = []

    for n_num in range(n):
        numbers = list(input().split())
        numbers = ' '.join(numbers)
        matrix.append(numbers)

    # print(n,m)
    pprint(matrix)

    for i in range(n-m+1):
        for j in range(n-m+1):
            result = []

            for row in range(m):
                a = ''
                for col in range(m):
                    # print(row,col)
                    a += matrix[i+row][j+col]
                    # print(a)
                result.append(a)
                
                for n in range(len(result)):
                    front = []
                    back = []
                    for start in range((m//2)):
                        front.append(result[n][start])
                        back.append(result[n][-(start+1)])
                print(front,back)

                if front == back :
                    print(f'#{tc} {''.join(front+back)}')




