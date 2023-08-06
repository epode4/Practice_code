import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    numbers = list(map(int,input().split()))

    numbers.sort()

    result = []
    while len(result) < 10:
        for i in range(len(numbers)):
            result.append(numbers[-(i+1)])
            result.append(numbers[i])
            
            if len(result) == 10:
                break
    
    result_total = ' '.join(map(str,result))
    print(f'#{tc} {result_total}')
        