def solution(strings, n):
    answer = []
    result = []
    for i in strings :
        answer.append([i[n],i[:n],i[n+1:]])
    answer.sort()
    for j in answer :
        result.append(j[1]+j[0]+j[2])
    return result