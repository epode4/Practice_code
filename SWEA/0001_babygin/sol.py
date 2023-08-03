import sys
sys.stdin = open('input.txt')

t = int(input())


for tc in range(1,t+1):

    triple = 0
    run = 0

    numbers = input()
    number = list(map(int,''.join(numbers)))
    number.sort()
    print(numbers)

    if number.count(number[0]) >= 3:
        triple += 1
    if number.count(number[-1]) >= 3:
        triple += 1

    if triple >= 1:
        if number[0]+1 == number[1] and number[0]+2 == number[2]:
            run += 1
        elif number[-1]-1 == number[-2] and number[-1]-2 == number[-3]:
            run += 1
            
    if triple ==1 and run ==1:
        print(f'#{tc} True')
    elif triple >= 2:
        print(f'#{tc} True')
    else: 
        print(f'#{tc} False')




    

