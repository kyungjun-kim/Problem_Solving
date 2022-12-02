# 문제 링크 https://www.acmicpc.net/problem/5597

T = list(map(lambda x : x , range(1,31)))
for i in range(28) :
    num = int(input())
    T.remove(num)
print(min(T))
print(max(T))