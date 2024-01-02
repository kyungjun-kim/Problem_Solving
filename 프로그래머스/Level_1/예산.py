def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for i in d :
        if total + i <= budget :
            total += i
            answer += 1
        else :
            break;
    return answer