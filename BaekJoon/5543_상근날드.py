# 문제링크 : https://www.acmicpc.net/problem/5543

b,d =[],[]
for i in range(5) :
    tmp = int(input())
    if i < 3 :
        b.append(tmp)
    else :
        d.append(tmp)
print(min(b) + min(d) -50)