def solution(arr):
    num = max(arr)
    answer = 0
    while True :
        answer += num
        #print(answer)
        if sum(list(map(lambda x : answer % x, arr))) == 0 :
            return answer
    return answer