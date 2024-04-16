def solution(polynomial):
    tmp, num = 0, 0
    for i in list(filter(lambda f : f != "+", polynomial.split())) :
        if i.isdigit() :
            num += int(i)
        else :
            if i == "x" :
                tmp += 1
            else :
                tmp += int(i.replace("x",""))
    if num == 0 :
        answer = "{}x".format(tmp)
    elif tmp == 0 :
        answer = "{}".format(num)
    else :
        answer = "{}x + {}".format(tmp,num)
    if answer[:2] == "1x" :
        answer = answer[1:]
    return answer