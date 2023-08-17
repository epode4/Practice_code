import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

t = int(input())


def my_sum(num,visited, sum_num):
    global min_sum
    if num >= n:
        if min_sum > sum_num:
            min_sum = sum_num
            return   

    if sum_num > min_sum:
        return     

    for i in range(n):
        if visited[i] == False:
            sum_num += (code[num][i])
            visited[i] = True
            my_sum(num+1,visited,sum_num)
            sum_num -= (code[num][i])
            visited[i] = False


for tc in range(1, t+1):
    n = int(input())
    code = [list(map(int,input().split())) for _ in range(n)]
        
    result = []
    visited = [False] * n

    min_sum = 1000000
    sum_num = 0

    my_sum(0,visited,sum_num)
    print(f'#{tc} {min_sum}')
