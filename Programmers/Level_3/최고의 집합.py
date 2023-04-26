# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12938#

def solution(n, s):
    if n > s :
        return [-1]
    answer = list(map(lambda x : s//n, range(n)))
    tmp = s % n
    idx = -1
    if sum(answer) != s :
        for i in range(tmp) :
            answer[idx] += 1
            idx -= 1
    return answer