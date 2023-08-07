import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    def paper(n):
        result = [1, 3]

        for i in range(1,int(n//10)-1):
            end1 = result[-2]
            end2 = result[-1]
            paper_num = 2*end1 + end2

            # print(end1, end2, paper_num)

            result.append(paper_num)
            # print(result)

        return result[-1]
    
    print(f'#{tc} {paper(n)}')        

