# 문제 링크 : https://www.acmicpc.net/problem/2675

T = int(input())
for i in range(T):
    S = list(map(str,input().split()))
    for j in range(len(S[1])):
        S.append(S[1][j]*int(S[0]))
    print(''.join(S[2:]))