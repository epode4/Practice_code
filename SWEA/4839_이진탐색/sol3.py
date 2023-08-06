import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1,t+1):
    p, a, b = map(int,input().split())
    left = 1
    right = p
    now = 0

    count_a = 0

    while now != a:          
        c = int((left + right)/2)

        if a >= c:
            left = c
        else:
            right = c
        now = c
        count_a += 1

    left = 1
    right = p
    now = 0
    count_b = 0

    while now != b:          
        c = int((left + right)/2)

        if b >= c:
            left = c
        else:
            right = c
        now = c
        count_b += 1

    # print(count_a, count_b)

    if count_a < count_b:
        print(f'#{tc} A')
    elif count_a > count_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
