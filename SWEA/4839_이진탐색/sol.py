import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1,t+1):
    # p = 전체 페이지, a = a가 찾을 페이지, b = b가 찾을 페이지
    p, a, b = map(int, input().split())
    # print(p, a, b)

    count_a = 0
    count_b = 0

    l = 1
    r = p 
    c = int((l+r)/2)

    while c != a:
        if a > c:
            l = c
        else:
            r = c

        c = int((l+r)/2)
        # print(l,r,c)
        count_a += 1
        

    l = 1
    r = p 
    c = int((l+r)/2)

    while c != b:
        if b > c:
            l = c
        else:
            r = c
                
        c = int((l+r)/2)
        # print(l,r,c)
        count_b += 1

    result = []
    if count_a < count_b:
        result = 'A'
    elif count_a > count_b:
        result = 'B'
    else:
        result = 0

    # print(count_a, count_b)

    print(f'#{tc} {result}')

