import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # v : 노드 개수 / e : 간선 개수 
    v, e = list(map(int,input().split()))

    nodes = [[0]*(v+1) for _ in range(v+1)]
    # pprint(nodes)

    for i in range(e):
        a, b = list(map(int, input().split()))
        nodes[a][b] = 1
        nodes[b][a] = 1

    # pprint(nodes)

    # s : 출발 노드 / g : 도착 노드
    s, g = list(map(int,input().split()))
    # print(s,g)

    # check_list = [False] * (v+1)
    queue = []

    now = s
    # check_list[now] = True
    queue.append(now)

    # 거리 계산을 위한 리스트
    distance = [0] * (v+1) 

    while len(queue):
        now = queue.pop(0)
        # check_list[now] = True

        # now와 연결된 다른 노드들 순회
        for i in range(v+1):
            if nodes[now][i] == 1:
                # 아직 방문하지 않은 node가 있다면 
                if not distance[i]:
                    # 큐에 추가
                    queue.append(i) 
                    # 이전 노드의 거리 + 1
                    distance[i] = distance[now] + 1
    print(distance)
    print(distance[g])
            