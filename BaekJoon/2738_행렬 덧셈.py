#문제 링크 : https://www.acmicpc.net/problem/2738
N,M = list(map(lambda x : int(x), input().split()))
A,B = [],[]
for i in range(N) :
    A.append(list(map(lambda x : int(x), input().split())))
for i in range(N) :
    B.append(list(map(lambda x : int(x), input().split())))
for i in list(map(lambda x,y : [str(i+j) for i,j in zip(x,y)], A,B)) :
    print(' '.join(i)