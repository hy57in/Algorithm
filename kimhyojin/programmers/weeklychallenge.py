def solution(price, money, count):
    fee = 0

    for i in range(1, count + 1):
        fee += price * i

    return fee - money if fee > money else 0