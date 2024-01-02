# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    d = {name: value for name, value in zip(players, range(len(players)))}
    dr = {name: value for name, value in zip(range(len(players)), players)}
    for c in callings :
        dr[d[c]-1], dr[d[c]] = c, dr[d[c]-1]
        d[c] -= 1
        d[dr[d[c]+1]]+=1
    return list(map(lambda l : l[0], sorted(d.items(), key=lambda x : x[1])))