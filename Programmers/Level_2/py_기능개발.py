# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math
def solution(progresses, speeds):
    answer,result = [], []
    d,num = 1,0
    for i,j in enumerate(progresses) :
        answer.append(math.ceil((100-j) / speeds[i]))
        if num < math.ceil((100-j) / speeds[i]) :
            num = math.ceil((100-j) / speeds[i])
            result.append(d)
            d = 1
        else :
            d += 1
    result.append(d)
    return result[1:]