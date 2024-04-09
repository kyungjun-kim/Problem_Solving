def solution(slice, n):
    cnt = 1
    if slice < n :
        while True :
            cnt += 1
            if cnt * slice >= n :
                return cnt          
    else :
        return 1