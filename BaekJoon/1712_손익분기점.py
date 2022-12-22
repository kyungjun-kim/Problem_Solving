# 문제 링크 : https://www.acmicpc.net/problem/1712

A, B, C = map(int, input().split())
#A = 고정비용,B = 가변비용, C = 가격
if (B >= C) :
    print(-1)
else :
    print(A//(C-B)+1)