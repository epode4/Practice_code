import sys
sys.stdin = open('input.txt')

t = 10

for tc in range(1,t+1):
    n = int(input())
    heights = list(map(int,input().split()))

    number = [-2,-1,1,2]
    view = 0

    for i in range(2, n-2):
        height = 0
        for num in number:
            # print(heights[i+num])
            if heights[i+num] > height:
                height = heights[i+num]
            # print(height)

        if heights[i] > height:
            view += (heights[i] - height)

    print(f'#{tc} {view}')

