result = []

for i in range(1,101):
    if i % 2 != 0:
        result.append(i)


print(', '.join(map(str,result)))