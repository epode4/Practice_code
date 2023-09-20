def solution(numbers):
    answer = []

    for idx_i, i in enumerate(numbers):

        numbers_1 = []
        for idx_x, x in enumerate(numbers):
            if idx_x != idx_i:
                numbers_1.append(x)

        for j in numbers_1:
            if i+j not in answer:
                answer.append(i+j)
    return sorted(answer)
