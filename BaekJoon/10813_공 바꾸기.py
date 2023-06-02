#문제 링크 : https://www.acmicpc.net/problem/10813
N,M = list(map(lambda x : int(x), input().split()))
basket = list(map(lambda x : x, range(1,N+1)))
for i in range(M) :
    i,j = list(map(lambda x : int(x)-1, input().split()))
    basket[i], basket[j] = basket[j], basket[i]
print(" ".join(list(map(lambda x : str(x) ,basket))))