# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    d = dict(map(lambda x : tuple(x.split()) , terms))
    p = list(map(lambda x : int(x.split()[0].split(".")[1])*28+int(x.split()[0].split(".")[2])+int(x.split()[0].split(".")[0])*336 +int(d.get(x.split()[1]))*28 , privacies))
    t = int(today.split(".")[0])*336 + int(today.split(".")[1])*28 + int(today.split(".")[2])
    answer = list(filter(lambda f : f >0, (map(lambda x,y : y+1 if x <= t else 0, p,range(len(p))))))
    return answer