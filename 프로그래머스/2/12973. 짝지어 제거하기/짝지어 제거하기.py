def solution(s):
    result = []
    for i in s :
        if result == [] or result[-1] != i :
            result.append(i)
        else :
            result.pop()
    return 1 if result == [] else 0