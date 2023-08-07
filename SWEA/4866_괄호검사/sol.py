import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    test = input()
    result = []

    for i in test:
        if i == '(':
            result.append(i)
        if i == ')' and result[-1] == '(':
            result.pop()

        if i == '{':
            result.append(i)
        if i == '}' and result[-1] == '{':
            result.pop()

    if len(result) >= 1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
