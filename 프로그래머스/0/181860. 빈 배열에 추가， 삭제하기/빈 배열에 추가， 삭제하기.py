def solution(arr, flag):
    answer = []
    for i,j in zip(arr,flag) :
        if j == True :
            answer += [i] * i * 2
        else :
            answer = answer[:-i]
    return answer