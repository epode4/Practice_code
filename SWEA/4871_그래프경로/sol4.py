import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    v, e = list(map(int,input().split()))

    nodes = [[] for _ in range(v+1)]

    for i in range(e):
        a, b = list(map(int,input().split()))
        nodes[a].append(b)

    s, g = list(map(int,input().split()))

    check_list = [False] * (v+1)
    stack = []

    now = s
    stack.append(now)
    check_list[now] = True

    result = 0

    while len(stack):

        now = stack.pop()
        check_list[now] = True

        for link in nodes[now]:
            if check_list[link] == False:
                stack.append(link)

                if link == g:
                    result = 1
    print(result)