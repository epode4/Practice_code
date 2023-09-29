def solution(babbling):
    answer = 0
    talking = ['aya', 'ye','woo','ma']
    
    for bab in babbling:
        for talk in talking: 
            if (talk*2) in bab:
                bab = ''               
            if talk in bab:
                bab = bab.replace(talk, ' ')
                if bab in ' '*30:
                    answer += 1
            
    return answer