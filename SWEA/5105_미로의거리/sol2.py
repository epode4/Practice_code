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

    # pprint(maze)

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = (i,j)

    # print(start)

    queue = []
    queue.append(start)
    
    now = start
    sum_way = 0

    dx = [0,0,1,-1]
    dy = [-1,1,0,0]

    while queue:
        now = queue.pop(0)
        x,y = now[0], now[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < n:
                if maze[nx][ny] == 0:
                    way = (nx, ny)
                    queue.append(way)
                    maze[nx][ny] = maze[x][y] -1

                elif maze[nx][ny] == 3:
                    sum_way = abs(maze[x][y] -2)                    
                    break



    # pprint(maze)
    print(f'#{tc} {sum_way}')
            
