def solution(cards1, cards2, goal):
    answer = 'Yes'
    card1 = []
    card2 = []
    for i in goal:
        if i in cards1:
            card1.append(cards1.index(i))
        else:
            card2.append(cards2.index(i))
            
    card_m = []
    for a in range(len(card1)-1):
        card_m.append(card1[a+1]-card1[a])
    
    for b in range(len(card2)-1):
        card_m.append(card2[b+1]-card2[b])
        
    
    for j in card_m:
        if j != 1:
            answer = 'No'

        
    return answer