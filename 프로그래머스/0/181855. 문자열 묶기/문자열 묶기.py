def solution(strArr):
    strArr = list(map(lambda x : len(x), strArr))
    answer = 1
    for i in set(strArr) :
        if strArr.count(i) > answer :
            answer = strArr.count(i)
    return answer