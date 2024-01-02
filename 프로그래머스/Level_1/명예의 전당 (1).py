# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/138477

import heapq
def solution(k, score):
    answer,result = [],[]
    for i in score :
        if len(result) >= k :
            if i > result[0] :
                heapq.heappop(result)
                heapq.heappush(result, i)
            else :
                answer.append(result[0])
                continue
        else :
            heapq.heappush(result, i)
        answer.append(result[0])
    return answer