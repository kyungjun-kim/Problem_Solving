def solution(code):
    m, answer = 0, ""
    for i,j in enumerate(code) :
        if m == 0 : 
            if j == "1" :
                m = 1
            elif j != "1" and i % 2 == 0 :
                answer += j
        elif m == 1 :
            if j == "1" :
                m = 0
            elif j != "1" and  i % 2 :
                answer += j
    return answer if len(answer) > 0 else "EMPTY"