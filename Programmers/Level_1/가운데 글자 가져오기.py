def solution(s):
    if len(s)%2:
        answer = s[int((len(s)-1)/2)]
    else :
        answer = s[int(len(s)/2-1):int((len(s)/2+1))]
    return answer