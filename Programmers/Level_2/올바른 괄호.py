# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    l,r,num = 0,0,0
    if s[0] == ")" or s[-1] == "(" :
        return False
    for i in s :
        if i == "(" :
            l += 1
            num += 1
        else :
            r += 1
            num -= 1
        if num < 0 :
            #print(num)
            return False
    if l != r :
        return False
    return True