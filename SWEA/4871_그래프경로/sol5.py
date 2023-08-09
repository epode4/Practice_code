# 인접리스트방식으로 그래프 저장 -> 재귀함수를 이용하여 풀이
import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

# stack을 안 쓰는 dfs
def dfs(now):
    # 방문체크
    check_list[now] = True
    print(check_list)

    # 현재 위치를 기준으로 연결된 노드 찾기
    for link in nodes[now]:
        print(link)
        # 방문하지 않은 노드들은 stack에 추가 -> 재귀함수 실행
        if not check_list[link]:
            dfs(link)


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

    dfs(s)

    if check_list[g]:
        result = 1
    else:
        result = 0

    print(result)