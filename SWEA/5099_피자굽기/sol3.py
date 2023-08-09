import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # n : 화덕 크기 / m : 피자 개수 
    n, m = list(map(int,input().split()))
    # ci : 각 피자별 치즈 양
    ci = list(map(int,input().split()))

    fire = []

    for i in range(n):
        fire.append([ci[0],i])
        ci.pop(0)

    print(fire)


    while len(fire) > 1:
        # print(fire)
        fire[0][0] = fire[0][0] // 2   

        if fire[0][0] == 0:
            fire.pop(0)
            if ci:
                fire.insert(0,ci[0])
                ci.pop(0)
            # print(fire)
        else:
            fire.pop(0)
            fire.append(fire[0])
            # print(fire)

        print(fire)
        


