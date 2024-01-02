# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    p = list(map(lambda x : [priorities[x],x], range(len(priorities))))
    answer = []
    cnt, tmp = 0,0
    while True :
        if p[tmp][0] == max(list(map(lambda x : x[0],p))) :
            answer.append(p[tmp])
            p.remove(p[tmp])
        else :
            tmp += 1
        cnt += 1
        if tmp == len(p) :
            tmp = 0
        if len(p) == 0 :
            break
    return list(map(lambda x : x[1], answer)).index(location) + 1