import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    numbers = list(map(int,input().split()))

    heap = [0] * (n+1)
    heap_size = 0 

    for i in range(n):
        # heap_size = 현재 마지막 노드 위치 
        heap_size += 1
        # 맨 마지막 노드에 삽입하려는 데이터를 할당
        heap[heap_size] = numbers[i]

        child_idx = heap_size
        parent_idx = child_idx // 2

        # heap의 조건에 맞도록 교환 반복
        while parent_idx and heap[parent_idx] > heap[child_idx]:
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]

            child_idx = parent_idx
            parent_idx = child_idx // 2

    # n = 마지막 노드  
    node = n // 2
    total = 0

    # 조상을 계속 찾아 올라가다 루트를 찾을 때까지
    while node:
        total += heap[node]
        node //= 2

    print(total)