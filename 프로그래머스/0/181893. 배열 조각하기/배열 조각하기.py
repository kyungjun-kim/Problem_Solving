def solution(arr, query):
    for i,q in enumerate(query) :
        if i % 2 :
            arr = arr[q:]
        else :
            arr = arr[:q+1]
    return arr