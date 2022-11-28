def solution(s):
    result = []
    for s in s.split(" ") :
        ss = ""
        for i in range(len(s)) :
            if i%2 == 0 :
                ss += s[i].upper()
            else : 
                ss += s[i]
        result.append(ss)
    return ' '.join(result)