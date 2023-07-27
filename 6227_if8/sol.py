# number = []

# for i in range(100,301):
#     if i // 100 == 2:
#         if ((i-200) // 10) % 2 == 0:
#             if i % 2 == 0:
#                 # print(i)
#                 number.append(i)

# numb = list(map(str,number))
# print(','.join(numb))


# 100, 10으로 나누면 float 타입이 되기 때문에 int로 변환 필요

result = []

for i in range(100,301):

    if int(i/100)% 2 == 0:
        if int(i/10)%2 == 0:
            if i%2 ==0:
                result.append(i)

num = list(map(str, result))
print(','.join(num))


# r = []
# for x in range(100,301):
#     a = int(x/100)
#     b = int(x/10)

#     if a%2 == 0 and b%2 == 0 and x%2 == 0:
#         r.append(str(x))
# print(",".join(r))
