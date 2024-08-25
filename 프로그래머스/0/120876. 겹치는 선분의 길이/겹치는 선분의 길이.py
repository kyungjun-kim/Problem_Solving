def solution(lines):
    answer = 0
    a = list(map(lambda x : list(range(x[0],x[1]+1)) , lines))
    for i in range(min(sum(a,[])),max(sum(a,[]))) :
        tmp = 0
        for j in a :
            if i in j and i+1 in j :
                tmp += 1
        if tmp > 1 :
            answer += 1
    return answer