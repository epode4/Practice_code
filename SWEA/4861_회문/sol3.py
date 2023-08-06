import sys
from pathlib import Path
from pprint import pprint
import math

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n, m = list(map(int, input().split()))

    string_map = []
    for tring in range(n):
        string_map.append(input()) # -> 'GOFFAKWFSM'(string)
        # string_map.append(list(input())) # -> ['G','O','F','F',...] (list)

    # pprint(string_map)
    result = []

    # 가로 기준점을 잡기 위한 코드 - 가로는 행 끝까지 돌아야함
    for row in range(n):
        for col in range(n-m+1):
            # print(string_map[row][col])

            for i in range(m//2):
                # front = 앞글자부처 한칸씩 증가
                f = string_map[row][col+i]
                # back = 뒷글자부터 한칸씩 감소
                b = string_map[row][col+m-1-i]

                # 앞뒤가 똑같을 때 
                if f == b:
                    continue
                # 앞뒤가 다를 때
                else:
                    break
            
            # for문을 끝까지 도는 경우(break를 끝까지 만나지 않는 회문을 찾은 경우)
            else:
                for a in range(m):
                    result.append(string_map[row][col+a])

    # 세로 기준점을 잡기 위한 코드
    for col in range(n):
        for row in range(n-m+1):

            for i in range(m//2):
                # front = 앞글자부처 한칸씩 증가
                f = string_map[row+i][col]
                # back = 뒷글자부터 한칸씩 감소
                b = string_map[row+m-1-i][col]

                # 앞뒤가 똑같을 때 
                if f == b:
                    continue
                # 앞뒤가 다를 때
                else:
                    break
            
            else:
                for a in range(m):
                    result.append(string_map[row+a][col])
        
    print(''.join(result))


