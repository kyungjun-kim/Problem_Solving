def solution(arr, queries):
    answer = []
    for s,e,k in queries :
        tmp = list(filter(lambda f : k < f, arr[s:e+1]))
        if len(tmp) < 1 :
            answer.append(-1)
        else :
            answer.append(min(tmp))
    return answer