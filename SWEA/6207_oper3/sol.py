import sys
sys.stdin = open('input.txt')

num = int(input())


result = num * 1.8 + 32

print(f'{num:.2f} ℃ =>  {result:.2f} ℉')