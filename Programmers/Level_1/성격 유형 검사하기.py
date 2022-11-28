def solution(survey, choices):
    answer = ''
    result = [0,0,0,0]
    p = [['R','T'],["C",'F'],["J","M"],["A","N"]]
    for i,j in zip(survey, choices):
        if "R" in i :
            if j == 4:
                continue
            elif bool(i.index("R")):
                result[0] += j - 4
            else :
                result[0] -= j - 4
        elif "C" in i :
            if j == 4:
                continue
            elif bool(i.index("C")):
                result[1] += j - 4
            else :
                result[1] -= j - 4
        elif "J" in i :
            if j == 4:
                continue
            elif bool(i.index("J")):
                result[2] += j - 4
            else :
                result[2] -= j - 4
        elif "A" in i :
            if j == 4:
                continue
            elif bool(i.index("A")):
                result[3] += j - 4
            else :
                result[3] -= j - 4
    for i,j in enumerate(zip(result,p)) :
        print(i,j, j[0])
        if j[0] >= 0 :
            answer += j[1][0]
        else :
            answer += j[1][1]
    return answer