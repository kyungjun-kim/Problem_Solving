# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42747#

def solution(citations):
    for i in range(len(citations),-1,-1) :
        if len(list(filter(lambda x : x >= i, citations))) >= i :
            return i
        