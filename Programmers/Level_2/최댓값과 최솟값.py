# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = list(map(int, s.split()))
    answer.sort()
    return str(min(answer)) + " " + str(max(answer))