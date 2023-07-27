import sys
sys.stdin = open('input.txt')

char = input()

if char.isupper():
    char2 = char.lower()
    print(f'{char}(ASCII: {ord(char)}) => {char2}(ASCII: {ord(char2)})')
elif char.islower():
    char2 = char.upper()
    print(f'{char}(ASCII: {ord(char)}) => {char2}(ASCII: {ord(char2)})')
else:
    print(char)
