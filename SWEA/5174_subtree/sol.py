import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # e: 간선 개수 / n : 서브 트리 시작 노드
    e, n = list(map(int,input().split()))

    numbers = list(map(int,input().split()))

    left = [0] * (e+2)
    right = [0] * (e+2)

    for i in range(0,len(numbers), 2):
        parent, child = numbers[i], numbers[i+1]
        # print(parent,son)
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    # print(left,right)

    stack = [n]
    count = 0

    while stack:
        now = stack.pop()
        count += 1

        if left[now]:
            stack.append(left[now])
        
        if right[now]:
            stack.append(right[now])


    print(count)
