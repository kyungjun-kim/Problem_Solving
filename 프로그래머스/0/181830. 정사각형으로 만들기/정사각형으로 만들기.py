def solution(arr):
    a,b = len(arr), len(arr[0])
    if a > b :
        for i in arr :
            for j in range(a - b) :
                i.append(0)
    elif a < b :
        for j in range(b - a) :
            arr.append([0 for x in range(b)])
    return arr