input = [88,30,61,55,95]

num = 0

for i in input:
    num += 1

    if i >= 60:
        print(f'{num}번 학생은 {i}점으로 합격입니다.')
        
    else:
        print(f'{num}번 학생은 {i}점으로 불합격입니다.')
        