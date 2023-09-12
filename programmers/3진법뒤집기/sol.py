def solution(n):
    
    def convert_notation(n):
        T = "0123456789ABCDEF"
        q, r = divmod(n, 3)

        result = (convert_notation(q) + T[r] if q else T[r])
        return result

    result = convert_notation(n)[::-1]

    result = int(result,3)
    return result


# print(convert_notation(45))
# print(convert_notation(125))
print(solution(45))
print(solution(125))


