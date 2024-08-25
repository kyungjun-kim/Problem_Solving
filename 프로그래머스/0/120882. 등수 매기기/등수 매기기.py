def solution(score):
    answer = []
    a = sorted(list(map(lambda x : x[0]+x[1] , score)),reverse=True)
    for i in score :
        answer.append(a.index(sum(i))+1)
    return answer