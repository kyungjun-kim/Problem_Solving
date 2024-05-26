def solution(arr, queries):
    for s, e in queries :
        arr = list(map(lambda x,y : x+1 if y in range(s,e+1) else x , arr, range(len(arr))))
    return arr