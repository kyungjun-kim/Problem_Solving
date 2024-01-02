# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    ny = dict(zip(name,yearning))
    return list(map(lambda x : sum(list(map(lambda y : ny[y] if y in ny else 0, x))) , photo))