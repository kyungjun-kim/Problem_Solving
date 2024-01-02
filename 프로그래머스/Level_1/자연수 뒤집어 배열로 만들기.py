def solution(n):
    a = list(map(int, list(str(n))))
    answer = []
    for i in range(len(a)-1,-1, -1) :
        answer.append(a[i])
    return answer