import sys
sys.stdin = open('input.txt')

num = int(input())

result = num * 2.2046

print(f'{num:.2f} kg =>  {round(result,2)} lb')