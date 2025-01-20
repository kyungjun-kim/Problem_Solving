def solution(wallet, bill):
    wallet = sorted(wallet)
    answer = 0
    while not(bill[0] <= wallet[0] and bill[1] <= wallet[1]) :
        a, b = max(bill) // 2, min(bill)
        if a > b :
            a,b = b,a
        bill = [a,b]
        answer += 1
    return answer