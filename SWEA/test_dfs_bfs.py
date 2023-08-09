nodes = [
[0,0,1,1,0,0],
[0,0,1,0,1,0],
[1,1,0,0,0,0],
[1,0,0,0,0,1],
[0,1,1,0,0,0],
[0,0,0,1,0,0]
]

n = 6

visited = [False] * n       # 정점에 방문했는지 상태 저장 (n = 정점 개수)

stack = []                  # 경로 역추적에 필요한 stack 구조

def dfs(v):                 # 시작 정점 v에서 시작
    visited[v] = True       # 방문한 정점의 상태 True로 표시
    stack.append(v)         # 방문한 정점의 정보 stack에 저장

    while len(stack):       # stack에 갈 정점이 남아있는 경우 반복
        v = stack.pop()     # stack의 최상단 정점으로 이동
        visited[v] = True   # 방문한 정점의 상태 True로 표시
        print(visited)
        print(stack)

        # 그래프 정보가 인접행렬방식으로 저장된 경우

        for link in range(n):         # 그래프 노드(정점) 수만큼 반복
            if nodes[v][link] == 1:   # 현재 정점과 연결된 정점 존재
                if not visited[link]: #연결된 정점 방문하지 않았다면
                    stack.append(link)  # stack에 정점 추가
                    

dfs(0)


visited = [False] * n       # 정점에 방문했는지 상태 저장 (n = 정점 개수)

queue = []                  # 경로 추적에 필요한 queue 구조

def bfs(v):                 # 시작 정점 v에서 시작
    visited[v] = True       # 방문한 정점의 상태 True로 표시
    queue.append(v)         # 방문한 정점의 정보 stack에 저장

    while len(queue):       # queue에 갈 정점이 남아있는 경우 반복
        v = queue.pop(0)    # queue의 첫번째 정점으로 이동
        visited[v] = True   # 방문한 정점의 상태 True로 표시
        print(visited)
        print(queue)

        # 그래프 정보가 인접행렬방식으로 저장된 경우

        for link in range(n):         # 그래프 노드(정점) 수만큼 반복
            if nodes[v][link] == 1:   # 현재 정점과 연결된 정점 존재
                if not visited[link]: #연결된 정점 방문하지 않았다면
                    queue.append(link)  # queue에 정점 추가

bfs(0)