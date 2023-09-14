# def solution(s):
#     answer = []
#     result = ''
#     s_split = s.split()
#     for i in s_split:
#         # print(s_split[i])
#         for j in range(len(i)):
#             # print(s_split[i][j])
#             if j%2:
#                 result += (i[j].lower())
#             else:
#                 result += (i[j].upper())
#         answer.append(result)
#         result = ''
#     return ' '.join(answer)


def solution(s):
    # 최종 결과값
    answer = ''
    # 단어별 저장
    result = ''
    # 단어별 인덱스
    count = 0

    for i in s:
        # 공백을 만날 경우 최종 결과에 공백 추가 & 인덱스 초기화
        if i == ' ':
            answer += ' '
            count = 0
        # 공백이 아닌 경우 count 통해서 해당 인덱스 짝홀수 판별
        else:
            if count%2:
                result += i.lower()
                count += 1
            else:
                result += i.upper()
                count += 1
            # 공백 만나기 전까지 결과 최종 결과에 추가 후 초기화
            answer += result
            result = ''
            
    return answer

print(solution("try hello world"))
print(solution(	"  TRy HElLo  WORLD "))