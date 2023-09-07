def solution(phone_number):
    answer = []
    phone_number = iist(phone_number)
    for i in range(0,len(phone_number)-4):
        answer.append('*')
        phone_number.pop(0)
        
    for i in phone_number:
        answer.append(i)
    
    answer = ''.join(answer)
    return answer

print(solution("01033334444"))