import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    k, n, m = map(int,input().split())
    bus_station = list(map(int,input().split()))

    # k = 한 번 충전으로 최대한 이동할 수 있는 수 
    # n = 종점 정류장 번호
    # m = 충전기가 설치된 정류장 개수 

    bus = 0
    charge = 0

    while bus < n:
        for i in range(bus+k, bus, -1):
            if i >= n:
                bus = n
                break
                
            if i in bus_station:
                bus = i
                charge += 1
                break
        else:
            charge = 0
            bus = n
            

    print(f'#{tc} {charge}')