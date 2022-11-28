import re
def solution(dartResult):
    num = []
    for j,i in enumerate(dartResult) :
        if i.isdigit() :
            if dartResult[j+1].isdigit() :
                continue
            elif dartResult[j-1].isdigit() :
                num.append(10)
            else :
                num.append(int(i))
        else :
            if i.isalpha() :
                if i == 'S' :
                    num[-1] = num[-1] ** 1
                elif i == 'D' :
                    num[-1] = num[-1] ** 2
                elif i == 'T' :
                    num[-1] = num[-1] ** 3
            else :
                if i == '*' :
                    num[-1] = num[-1] * 2
                    if len(num) > 1 :
                        num[-2] = num[-2] * 2
                elif i == '#' :
                    num[-1] = num[-1] * -1
    return sum(num)