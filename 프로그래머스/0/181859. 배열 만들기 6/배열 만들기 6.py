def solution(arr):
    stk = []
    for i in arr :
        if stk == [] :
            stk.append(i)
        else :
            if stk[-1] == i :
                stk.pop()
            else :
                stk.append(i)
    return stk if stk != [] else [-1]