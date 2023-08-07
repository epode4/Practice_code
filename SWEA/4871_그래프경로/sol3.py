import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    v, e = list(map(int,input().split()))

    matrix = [ [0] * (v+1) for _ in range(v+1)]
    # pprint(matrix)

    for i in range(e):
        x, y = list(map(int,input().split()))
        matrix[x][y] = 1

    # pprint(matrix)

    check_list = [False] * (v+1)
    stack = []

    s, g = list(map(int,input().split()))

    now = s
    check_list[now] = True
    stack.append(now)

    result = 0

    while len(stack):

        now = stack.pop()
        check_list[now] = True

        for i in range(v+1):
            if matrix[now][i] == 1:
                if check_list[i] == False:
                    stack.append(i)

                    if i == g:
                        result = 1
    print(result)
        