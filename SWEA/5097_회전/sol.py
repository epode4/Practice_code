import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n, m = list(map(int,input().split()))

    numbers = list(map(int,input().split()))

    # 직접 n번 반복
    for _ in range(m):
        numbers.append(numbers[0])
        numbers.pop(0)
        # print(numbers, len(numbers))

    print(f'#{tc} {numbers[0]}')

    
    # remain = m % n
    # print(f'#{tc} {numbers[remain]}')

    