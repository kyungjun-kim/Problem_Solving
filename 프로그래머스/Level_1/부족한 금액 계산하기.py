def solution(price, money, count):
    answer = - money
    for i in range(price, price*count+1, price):
        answer += i
    if answer <= 0 :
        return 0
    else :
        return answer