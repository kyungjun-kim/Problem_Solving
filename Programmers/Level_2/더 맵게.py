# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(s, K):
    cnt = 0
    s.sort()
    while s[0] < K :
        if len(s) <= 1 :
            return -1
        else :
            a = heapq.heappop(s)
            b = heapq.heappop(s)
            heapq.heappush(s, (a + (2*b)))
            cnt += 1
    return cnt