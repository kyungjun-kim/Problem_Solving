def solution(arr, n):
    if len(arr) % 2 :
        return list(map(lambda x,y : x+n if y%2 == 0 else x, arr, range(len(arr))))
    else :
        return list(map(lambda x,y : x+n if y%2 else x, arr, range(len(arr))))