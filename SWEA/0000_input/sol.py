import sys
sys.stdin = open('input.txt')

# N = int(input())

# if N % 2 == 1:
#     print('홀수입니다.')
# else:
#     print('짝수입니다.')

TC = int(input())

for i in range(TC):
    N = int(input())

    if N % 2 == 1:
        print('홀수')
    else:
        print('짝수')

# 1차원 리스트 input 받기
# numbers = input().split()
# print(numbers)

# for number in numbers:
#     int_num = int(number)
    
#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다')
    

# map : split()의 요소를 하나씩 int로 감싸주는 역할
numbers = list(map(int, input().split()))
print(numbers)

for number in numbers:
    if number % 2 == 1:
        print(f'{number}는 홀수입니다.')

# 2차원 리스트 input 받기

N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int,input().split()))
    matrix.append(numbers)

for row in matrix:
    # print(row)
    for item in row:
        if item == 5:
            print('5가 있습니다')