# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131705

from itertools import combinations
def solution(number):
    result = list(map(lambda x : sum(x), combinations(number, 3)))
    return len(list(filter(lambda s : s==0 , result)))