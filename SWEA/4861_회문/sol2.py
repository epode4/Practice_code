import sys
from pathlib import Path
from pprint import pprint
import math

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    strings = [input() for _ in range(N)]
    string_col = list(zip(*strings)) #행열변환

    result = ''
    for i in range(N):
        #row비교
        for j in range(N-M+1):
            if strings[i][j:j+M] == strings[i][j:j+M][::-1]:
                result = strings[i][j:j+M]
        #col비교
        for k in range(N-M+1):
            if string_col[i][k:k+M] == string_col[i][k:k+M][::-1]:
                result = ''.join(string_col[i][k:k+M])

    print(f'#{tc} {result}')