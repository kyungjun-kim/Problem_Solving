def solution(n):
    if n % 2 :
        answer = '수박' * int((n-1)/2) + '수'
    else : 
        answer = '수박' * int(n/2)
    return answer