# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    a = list(map(lambda x : False if x < 2 else True ,range(n+1)))
    for i in range(2,n+1) :
        if a[i] :
            answer += 1
            for j in range(2*i, n+1, i) :
                a[j] = False
    return sum(a)
