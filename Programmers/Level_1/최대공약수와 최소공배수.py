def solution(n, m):
    answer = []
    min_n = 0
    max_n = 0
    if n > m : n,m = m,n
    if m%n == 0 :
        answer.append(n)
        answer.append(m)
    else :
        for i in range(1,n+1) :
            if n%i == 0 and m%i == 0 :
                min_n = i
        answer.append(min_n)
        answer.append(m*n/ min_n)
    return answer