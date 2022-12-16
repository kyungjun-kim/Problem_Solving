# 문제 링크 : https://www.acmicpc.net/problem/5622

a = input()
answer = 0
for i in tuple(a) :
    #print(i,ord(i), (ord(i)-64)//4)
    answer += 2
    if ord(i) < 80 :
        #print(i,(ord(i)-65)//3)
        answer += (ord(i)-65)//3 + 1 
    else :
        if ord(i) < 84 :
            answer += 6
        elif ord(i) < 87 :
            answer += 7
        elif ord(i) < 91 :
            answer += 8
        else :
            answer += 9
print(answer)
