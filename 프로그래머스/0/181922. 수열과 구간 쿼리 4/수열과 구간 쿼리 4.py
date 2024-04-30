def solution(arr, queries):
    answer = []
    for s, e, k in queries :
        arr = list(map(lambda x,y : x+1 if y % k == 0 and s <= y <= e  else x , arr, range(len(arr))))
    return arr