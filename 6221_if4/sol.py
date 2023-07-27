import sys
sys.stdin = open('input.txt', encoding='utf-8')

m1 = input()
m2 = input()

# index 사용

rcp = ['가위', '바위', '보']
m1_idx = rcp.index(m1)
m2_idx = rcp.index(m2)

result = m1_idx - m2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
elif result < 0:
    if result == -1:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')


# m1 = input()
# m2 = input()

# rcp = ['가위', '바위', '보']
# m1_idx = rcp.index(m1)
# m2_idx = rcp.index(m2)

# result = m1_idx - m2_idx

# if result > 0:
#     print(f'Result : Man{result} Win!')
# elif result < 0:
#     if result == -1:
#         print('Result : Man2 Win!')
#     else:
#         print('Result : Man1 Win!')
# else:
#     print('Result : Draw')