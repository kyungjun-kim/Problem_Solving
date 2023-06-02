# 문제링크 : https://www.acmicpc.net/problem/2754

N = str(input())
answer = 0
if N == 'F' :
    print(0.0)
else :
    if N[0] == "A" :
        answer += 4
    elif N[0] == "B" :
        answer += 3
    elif N[0] == "C" :
        answer += 2
    elif N[0] == "D" :
        answer += 1
    if N[1] == "+" :
        answer += 0.3
    elif N[1] == "-" :
        answer -= 0.3
    print(float(answer))