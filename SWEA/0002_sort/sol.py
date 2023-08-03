my_list = [1, 3, 6, 7, 5,1, 9, 3]

# 버블정렬 : 원본데이터 직접 정렬
# 카운팅정렬 : 새로운 정렬 배열 return

# 버블정렬
for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            # print(my_list)
print(my_list)


#카운틴정렬
counter = [0 for i in range(10)]

for i in my_list:
    counter[i] += 1

result = []

for data, count in enumerate(counter):
    for i in range(count):
        result.append(data)

print(result)