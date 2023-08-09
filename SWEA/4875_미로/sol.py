import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    ground = []
    for i in range(n):
        a = list(map(str,input().split()))
        b = list(map(int,''.join(a)))
        ground.append(b)

    pprint(ground)

    stack = []
    check_list = [False] * n

    select = []

    for i in range(n):
        for j in range(n):
            if ground[i][j] != 1:
                select.append((i,j))
            if ground[i][j] == 2:
                start = (i,j)
            elif ground[i][j] == 3:
                end = (i,j)
    print(select,start,end)

    now = start

    

