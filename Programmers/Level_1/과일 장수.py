#문제 풀이 : https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score):
    answer = 0
    s = sorted(score,reverse=True)
    for i in range(0,len(s),m) :
        if len(s[i:i+m]) == m :
            answer += s[i+m-1] * m
        else :
            return answer
    return answer