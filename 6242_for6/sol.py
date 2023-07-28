blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

count_a = 0
count_b = 0
count_o = 0
count_ab = 0

for i in blood_type:
    if i == 'A':
        count_a += 1
    elif i == 'B':
        count_b += 1
    elif i == 'O':
        count_o +=1
    else:
        count_ab +=1

dict_b = {
    'A': count_a,
    'O': count_o,
    'B': count_b,
    'AB': count_ab,
}

print(dict_b)