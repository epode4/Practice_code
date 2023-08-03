import sys
sys.stdin = open('input.txt')

t = 10

for tc in range(1,t+1):
    n = int(input())
    height = list(map(int,input().split()))

    total_view = 0

    for i in range(2,n-2):

        left_height = 0
        right_height = 0

        if height[i] > height[i-1] and height[i] > height[i-2]:
            left_height = max(height[i-2], height[i-1])
            if height[i-1] == 0 and height[i-2] == 0:
                left_height = 1
        
        if height[i] > height[i+1] and height[i] > height[i+2]:
            right_height = max(height[i+2], height[i+1])
            if height[i+1] == 0 and height[i+2] == 0:
                right_height = 1

        # print(left_height, right_height)
        
        if left_height !=0 and right_height != 0:
            view = height[i]-max(left_height, right_height)
        else:
            view = 0
        # print(view)
        total_view += view

    print(f'#{tc} {total_view}')
