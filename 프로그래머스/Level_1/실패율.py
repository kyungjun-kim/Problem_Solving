def solution(N, stages):
    answer = list([0,len(stages),x+1,x+1] for x in range(N))
    num = 0
    stages.sort()
    cnt = 0
    for i in range(1,N+1) :
        for j in stages :
            if j > i :
                continue
            else :
                answer[i-1][0] += 1
        if i > 1 :
            answer[i-1][0] -= sum(list(x for x,y,z,a in answer[:i-1]))
        answer[i-1][1] -= num 
        num += answer[i-1][0]
        if answer[i-1][1] != 0 :
            answer[i-1][2] = answer[i-1][0] / answer[i-1][1]
        else : answer[i-1][2] = 0
    answer = list(a for x,y,z,a in sorted(answer, key=lambda x : x[2] , reverse = True))
    return answer