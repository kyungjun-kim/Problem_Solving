# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    result,answer = [],[]
    for i in range(len(s)) :
        if s[i] not in result :
            result.append(s[i])
            answer.append(-1)
        else :
            answer.append(len(result) - result.index(s[i]))
            result[result.index(s[i])] = '_'
            result.append(s[i])
    return answer