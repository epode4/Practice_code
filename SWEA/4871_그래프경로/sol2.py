# 인접리스트방식으로 그래프 저장
import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # v : 노드 수 / e : 간선 수
    v, e = list(map(int,input().split()))

    # 인덱스 번호와 노드 수 맞추기 위해서 v+1 으로 설정
    nodes = [[]  for _ in range(v+1)]
    # pprint(nodes)

    # 간선의 개수만큼 반복 진행행
    for line in range(e):
        start, end = list(map(int, input().split()))
        nodes[start].append(end)
    pprint(nodes)

    # s : 출발 노드 / g : 도착 노드
    s, g = list(map(int,input().split()))

    check_list =[False] * (v+1)
    stack = []

    now = s
    check_list[now] = True
    stack.append(now)

    result = 0

    while len(stack):
        # print()
        now = stack.pop()
        check_list[now] = True

        # 인접리스트를 기준으로 now와 연결된 link 노드들을 반복
        for link in nodes[now]:
            print(link)

            if not check_list[link]:
                if link == g:
                    result = 1

                stack.append(link)


    print(result)

