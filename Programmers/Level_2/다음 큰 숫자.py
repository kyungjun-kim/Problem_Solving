# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = n+1
    while bin(n).count("1") != bin(answer).count("1") :
        answer += 1
    return answer