def solution(n):
    answer = 1
    cnt = 1
    while answer <= n :
        cnt += 1
        answer *= cnt
        #print(answer, cnt)        
    return cnt - 1

#def fac(num) :
    
