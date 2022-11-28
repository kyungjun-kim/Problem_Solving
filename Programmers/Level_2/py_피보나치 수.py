# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    if n <= 2 :
        return 1
    one, two, result = 1,1,-1
    for i in range(3,n+1) :
        result = one + two
        one = two
        two = result
    return result % 1234567

