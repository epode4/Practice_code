import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx, visited, SUM):
    global min_SUM
    if idx >= n:
        if SUM < min_SUM:
            min_SUM = SUM
        return

    if SUM > min_SUM:
        return

    # 최소 합 찾기
    for i in range(n):
        if visited[i] == False:                
            # print(idx,i, '=', numbers[idx][i])
            # result.append(numbers[idx][i])
            SUM += numbers[idx][i]
            visited[i] = True
            search(idx+1, visited, SUM)
            # result.pop()
            SUM -= numbers[idx][i]
            visited[i] = False

for tc in range(1, T+1):
    n = int(input())

    numbers = []
    for _ in range(n):
        number = list(map(int,input().split()))
        numbers.append(number)

    result = []
    visited = [False] * n

    SUM = 0
    min_SUM = 10000000000


    search(0,visited, SUM)

    print(min_SUM)


        

        

