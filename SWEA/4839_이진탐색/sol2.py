import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1,T+1):
    # p : 책의 마지막 페이지
    # a : A가 찾아야 하는 목적 페이지
    # b : B가 찾아야 하는 목적 페이지
    p, a, b = list(map(int,input().spllit()))

    count_a = 0
    left = 1
    right = p

    while True:
        middle = int((left+right)/2)

        # 목적 페이지가 가운데보다 왼쪽에 있는 경우
        if a < middle:
            right = middle
        # 목적 페이지가 가운데보다 오른쪽에 있는 경우
        elif a >  middle:
            left = middle
        #둘 다 아니라면 목적 페이지에 도착
        else:
            break

        count_a += 1

    count_b = 0
    left = 1
    right = p

    while True:
        middle = int((left+right)/2)

        # 목적 페이지가 가운데보다 왼쪽에 있는 경우
        if b < middle:
            right = middle
        # 목적 페이지가 가운데보다 오른쪽에 있는 경우
        elif b >  middle:
            left = middle
        #둘 다 아니라면 목적 페이지에 도착
        else:
            break

        count_b += 1