def solution(n, lost, reserve):
    answer = n
    r = sorted(list(set(reserve).difference(lost)))
    l = sorted(list(set(lost).difference(reserve)))
    a = 0 
    for i in l :
        if i in r :
            r.remove(i)
        elif i-1 in r :
            r.remove(i-1)
        elif i+1 in r :
            r.remove(i+1)
        else :
            a+=1
        print(l,r)
    return n - a