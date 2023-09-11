# def solution(n):
    
def convert_notation(n):
    T = "0123456789ABCDEF"
    q, r = divmod(n, 3)

    result = (convert_notation(q) + T[r] if q else T[r])
    # return result
    result_1 = ''
    for i in result:
        result_1 = i + result_1

    return result_1

print(convert_notation(45))
print(convert_notation(125))
