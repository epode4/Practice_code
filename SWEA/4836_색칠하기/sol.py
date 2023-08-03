import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    color1 = []
    color2 = []
    count = 0

    for i in range(n):
        # numbers =  r1, c1, r2, c2, color
        numbers = list(map(int,input().split()))
        # print(numbers)

        for i in range(numbers[0], numbers[2]+1):
            for j in range(numbers[1], numbers[3]+1):
                if numbers[4] == 1:
                    color1.append((i,j))
                else:
                    color2.append((i,j))

    # print(color1)
    # print(color2)

        
    for num in color1:
        if num in color2:
            count += 1

    print(f'#{tc} {count}')