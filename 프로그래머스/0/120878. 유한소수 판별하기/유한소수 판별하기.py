def solution(a, b):
    while True :
        for i in range(min(a,b),1,-1) :
            if a % i == 0 and b % i == 0 :
                a //= i
                b //= i
                continue
        break
    while True :
        if b == 1 :
            return 1
        tmp = b
        if b % 5 == 0 :
            b //= 5
        if b % 2 == 0 :
            b //= 2
        if tmp == b :
            return 2