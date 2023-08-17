import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    maze = [list(map(int,input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze [i][j] == 2:
                start = (i,j)

    stack = []
    stack.append(start)

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    result = 0

    while len(stack):

        now = stack.pop()
        x, y = now[0], now[1]

        maze[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny <n:
                if maze[nx][ny] == 0:
                    stack.append((nx,ny))

                elif maze[nx][ny] == 3:
                    result = 1
                    break

    print(f'#{tc} {result}')

            
        

    
