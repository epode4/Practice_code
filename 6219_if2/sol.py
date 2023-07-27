import sys
sys.stdin = open('input.txt')

num = int(input())
number = []

for i in range(1, num+1):
    if num % i == 0:
        print(f'{i}(은)는 {num}의 약수입니다.') 
        number.append(i)  

if len(number) == 2:
    print(f'{num}(은)는 {number[0]}과 {number[1]}로만 나눌 수 있는 소수입니다.')

    