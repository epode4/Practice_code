import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    numbers = list(map(int,input().split()))

    tree = [0]

    tree.append(numbers.pop(0))

    for i in range(1,len(numbers)+1):
        tree.append(numbers.pop(0))

        if tree[i] < tree[i//2]:
            a = tree[i]
            tree[i] = tree[i//2]
            tree[i//2] = a
           
            
# python 내장함수 heapq.heapify
        