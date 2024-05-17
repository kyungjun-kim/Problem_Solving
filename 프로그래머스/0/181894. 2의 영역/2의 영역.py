def solution(arr):
    a = ','.join(list(map(lambda x : str(x), arr)))
    if "2" not in a :
        return [-1]
    else :
        return list(map(lambda x : int(x), a[a.index("2"):a.rindex("2")+1].split(",")))