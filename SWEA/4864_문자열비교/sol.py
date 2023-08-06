import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    first = list(input().split())
    first = ''.join(first)
    second = list(input().split())
    second = ''.join(second)
    count = 0
    
    for i in range(len(second)-len(first)+1):
        result = []
        for j in range(len(first)):
            if first[j] == second[i+j]:
                result.append(second[i+j])

        result_2 = ''.join(result)
        if first == result_2:
            count += 1

    if first == result_2:
        print(f'#{tc} {count}')
    else:
        print(f'#{tc} {count}')

