import sys
sys.stdin = open('input.txt')

num = int(input())
result = []

for n in range(1, num+1):
    if num % n == 0:
        print(f'{n}(은)는 {num}의 약수입니다.')
        result.append(n)
    if len(result) == 2:
        print(f'{num}(은)는 {result[0]}과 {result[1]}로만 나눌 수 있는 소수입니다.')
