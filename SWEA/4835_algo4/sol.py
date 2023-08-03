import sys
sys.stdin =open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    numbers = list(map(int,input().split()))
    
    sum =[]

    for i in range(1, n-m+2):
        total = 0
        for j in range(i):
            # print(i,j)
            total = numbers[j]
        sum.append(total)
        print(sum)
        

