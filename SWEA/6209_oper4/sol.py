import sys
sys.stdin = open('input.txt')

num = int(input())


result = (num-32) / 1.8

print(f'{num:.2f} ℉ =>  {result:.2f} ℃')