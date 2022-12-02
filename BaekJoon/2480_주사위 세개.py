# 문제 링크 : https://www.acmicpc.net/problem/2480

a = list(map(lambda x : int(x), input().split()))
if len(set(a)) == 3 :
    print(max(a) * 100)
elif len(set(a)) == 2 :
    print(1000+ sorted(list(map(lambda x : x if a.count(x) == 2 else 0, a)))[-1]*100)
else :
    print(10000 + a[0] * 1000)