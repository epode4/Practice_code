import sys
sys.stdin = open('input.txt')

num = int(input())

for n in range(1, num+1):
    if num % n == 0:
        print(f'{n}(은)는 {num}의 약수입니다.')
    