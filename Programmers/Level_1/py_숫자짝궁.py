# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    result = ''
    for i in list(map(lambda x : str(x), range(9,-1,-1))) :
        if i in X and i in Y :
            result += i * min(X.count(i), Y.count(i))
    if result == '' :
        return "-1"
    elif set(result) == {'0'} :
        return "0"
    else :
        return result 