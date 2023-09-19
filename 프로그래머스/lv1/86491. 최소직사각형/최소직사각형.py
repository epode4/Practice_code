def solution(sizes):

    width = list(i[0] for i in sizes)
    length = list(i[1] for i in sizes)

    # max_n = max((max(width), max(length)))

    for i in range(len(width)):
        if width[i] < length[i]:
            width[i], length[i] = length[i], width[i]

    return max(width)*max(length)