import sys
sys.stdin = open('input2.txt')

num = int(input())
word = input()

if word.isupper():
    print(f'#{num} {word} 는 대문자 입니다.')
else:
    print(f'#{num} {word} 는 소문자 입니다.')
