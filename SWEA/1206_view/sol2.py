import sys
sys.stdin = open('input.txt')

t = 10

for tc in range(1,t+1):
    n = int(input())
    building_list = list(map(int,input().split()))
    total = 0

    for i in range(n):
        now = building_list[i]

        # 현재 위치에 건물이 없다면 다음 건물로 이동
        if now == 0:
            continue

        # 나의 위치에 건물이 있는 경우
        else:
            # 양옆 건물 2개씩 높이 비교

            dx = [-2, -1, 1, 2]

            max_tall = 0

            for j in range(4):
                # i : 현재 위치 
                # dx[j] : 기준 건물 중심으로 좌우 인덱스 
                comp = building_list[i+dx[j]]

                if max_tall < comp:
                    max_tall = comp

            # 나머지 4개의 건물보다 내가 더 크다면 조망권 확보
            if now > max_tall:
                view = now - max_tall
                total += view

    
    print(f'#{tc} {total}')
        