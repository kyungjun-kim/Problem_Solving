# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12927#

def solution(n, works):
    if n >= sum(works) :
        return 0
    works = sorted(works , key = lambda k : -k)
    while n > 0 :
        for i in range(works.count(max(works))) :
            if n > 0 :
                works[i] -= 1
                n -= 1
            else :
                break
    return sum(list(map(lambda x : x**2, works)))