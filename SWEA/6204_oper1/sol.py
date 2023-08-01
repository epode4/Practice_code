import sys
sys.stdin = open('input.txt')

num = int(input())

result = num * 2.54

print(f'{num:.2f} inch =>  {result} cm')