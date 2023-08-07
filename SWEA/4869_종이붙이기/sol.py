import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    result = 0

    case = [1]

    i = (n//20)

    if i >= 0:
        result += case[0]
        print(n,result)
    if i >= 1:
        case.append(2)
        result += case[-1]*int(n/10-1)
        print(n, result)
    if i >= 2:
        case.append(4)
        result += case[-1]*(sum(range((int(n/10)-2))))
        print(n, result)
    if i >= 3:
        case.append(8)
        result += case[-1]*(sum(range((int(n/10)-4))))
        print(n, (sum(range((int(n/10)-4)))))


    print(result)



