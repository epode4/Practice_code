num = range(100,301)
number = []


for i in num:
    if i // 100 == 2:
        if ((i-200) // 10) % 2 == 0:
            if i % 2 == 0:
                # print(i)
                number.append(i)

numb = list(map(str,number))
print(','.join(numb))


