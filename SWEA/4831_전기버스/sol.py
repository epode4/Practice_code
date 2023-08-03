import sys
sys.stdin = open('input.txt')

t = int(input())

# n = 정류장 번호 / k = 이동 가능한 정류장 수 / m = 충전기 설치된 정류장

for tc in range(1, t+1):

    
    result = 0

    numbers = list(map(int,input().split()))
    m_count = list(map(int,input().split()))
    k = numbers[0]
    n = numbers[1]
    m = numbers[2]

    go = k

    
    while go <= n-k:
        for i in m_count:
            if i <= go:
                go = i + k
                result += 1
            else: 
                result = 0
                go += k

    if m_count[0] < k:
        result -= 1

            
    print(numbers)
    print(m_count)
    print(f'#{tc} {result}')