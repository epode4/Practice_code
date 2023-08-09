import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx, visited):
    if idx >= n:
        print(result)
        return

    # 세로 한 줄에 하나씩만 선택하는 경우
    for i in range(n):
        if visited[i] == False:                
            # print(idx,i, '=', numbers[idx][i])
            result.append(numbers[idx][i])
            visited[i] = True
            search(idx+1, visited)
            result.pop()
            visited[i] = False

for tc in range(1, T+1):
    n = int(input())

    numbers = []
    for _ in range(n):
        number = list(map(int,input().split()))
        numbers.append(number)

    result = []
    visited = [False] * n

    search(0,visited)


        

        

