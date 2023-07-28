# blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

# count_a = 0
# count_b = 0
# count_o = 0
# count_ab = 0

# for i in blood_type:
#     if i == 'A':
#         count_a += 1
#     elif i == 'B':
#         count_b += 1
#     elif i == 'O':
#         count_o +=1
#     else:
#         count_ab +=1

# dict_b = {
#     'A': count_a,
#     'O': count_o,
#     'B': count_b,
#     'AB': count_ab,
# }

# print(dict_b)

# 다른 방법 

blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A': 0,
    'O': 0,
    'B': 0,
    'AB': 0,
}

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)

# 어떤 요소가 들어올지 몰라서 미리 dict을 만들 수 없는 경우

# location_list = ['서울', '부산', '서울', '서울', '대전', '굉주']

# location_dict = {}

# for location in location_list:
#     # 이미 기록을 한 경우
#     if location in location_dict.keys():
#         location_dict[location] += 1
#     # 처음 등장한 경우
#     else:
#         location_dict[location] = 1

# print(location_dict)