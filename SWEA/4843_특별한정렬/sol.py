import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int,input().split()))

    result = []


    for _ in range(5):
                
        max_num = 0
        min_num = 10000
        for i in range(len(numbers)):
            if numbers[i] > max_num:
                max_num = numbers[i]
            
        result.append(max_num)
        # print(result, numbers, max)
        numbers.remove(max_num)

        for i in range(len(numbers)):
            if numbers[i] < min_num:
                min_num = numbers[i]
        
  
        result.append(min_num)
        numbers.remove(min_num)
        
    l = ' '.join(map(str,result))
    print(f'#{tc} {l}')

    #min, max 써서 넣기
    # 정렬해서 뽑기