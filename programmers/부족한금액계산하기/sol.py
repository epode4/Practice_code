def solution(price, money, count):
    price_n = price
    for i in range(1,count+1):
        money -= price_n
        price_n += price

    return abs(min(money,0))

print(solution(3,20,4))