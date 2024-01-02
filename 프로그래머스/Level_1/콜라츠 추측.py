def solution(num):
    n = num
    cnt = 0
    while(n != 1) :
        if n == 1 :       
            break
        if n % 2 == 0:
            n = n/2
            cnt += 1
        else :
            n = n*3 + 1
            cnt += 1
        if cnt == 500 :
            return -1
    return cnt