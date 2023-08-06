import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int,''.join(input())))
    

    test = [ 0 for _ in range(10)]

    for i in numbers:
        test[i] += 1

    max_num = max(test)
    max_card = 0

    for i in range(len(test)):
        if test[i] == max_num:
            max_card = i

    print(f'#{tc} {max_card} {max_num}')