#인접행렬방식으로 그래프 저장
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
    nodes = [[0]*(v+1)  for _ in range(v+1)]
    # pprint(nodes)

    # 간선의 개수만큼 반복 진행행
    for line in range(e):
        start, end = list(map(int, input().split()))
        nodes[start][end] = 1
    pprint(nodes)

    # s : 출발 노드 / g : 도착 노드
    s, g = list(map(int,input().split()))

    # 방문 체크용 리스트
    check_list = [False] * (v+1)
    # print(check_list)

    # dfs를 구현하기 위한 stack
    stack = []

    # 방문한 곳은 True로 체크하고 stack에 추가
    now = s
    check_list[now] = True
    stack.append(now)

    result = 0

    # stack이 비어있지 않으면 계속 반복
    while len(stack):

        # 제일 위에 있는 거 뽑아서 거기로 이동
        now = stack.pop()
        check_list[now] = True

        for link in range(v+1):

            # now를 기준으로 연결되어 있다면
            if nodes[now][link] == 1:
                # 방문하지 않았다면(check_list가 False라면)
                if not check_list[link]:
                    if link == g:
                        result = 1

                    # stack에 추가
                    stack.append(link)

    print(result)