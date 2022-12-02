# 문제 링크 : https://www.acmicpc.net/problem/25304

s = int(input())
n = int(input())
result = 0
for i in range(n) :
    tmp = list(map(lambda x : int(x), input().split()))
    result += tmp[0] * tmp[1]
if s == result :
    print("Yes")
else :
    print("No")