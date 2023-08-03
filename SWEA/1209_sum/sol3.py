import sys
sys.stdin = open('input.txt')
from pprint import pprint

t = 10

for tc in range(1,t+1):
    tc = int(input())

    
    matrix = []

    for i in range(100):
        matrix.append(list(map(int,input().split())))
        

    total_sum = 0

    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[0])):
            sum += matrix[i][j]

        if sum > total_sum:
            total_sum = sum
    
    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]

        if sum > total_sum:
            total_sum = sum
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]

        if sum > total_sum:
            total_sum = sum
    sum = 0 
    for i in range(len(matrix)):
        sum = 0
        sum += matrix[i][-i]

        if sum > total_sum:
            total_sum = sum
            
    print(f'#{tc} {total_sum}')