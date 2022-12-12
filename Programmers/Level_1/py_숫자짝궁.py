# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    result = []
    num = list(map(lambda x : str(x), range(10)))
    for i in num :
        if i in X and i in Y :
            tmp = [i]
            result.extend(tmp * min(X.count(i), Y.count(i)))
            X,Y = X.replace(i,'',1), Y.replace(i,'',1)
    if result == [] :
        return "-1"
    elif set(result) == {'0'} :
        return "0"
    else :
        return ''.join(sorted(result, reverse = True))