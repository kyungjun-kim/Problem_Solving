#문제링크 : https://www.acmicpc.net/problem/10810

N,M = list(map(lambda x : int(x), input().split()))
basket = list(map(lambda x : 0, range(N)))
for i in range(M) :
    i,j,k = list(map(lambda x : int(x), input().split()))
    basket = list(map(lambda x : k if i-1 <= x <= j-1 else basket[x] , range(N)))
print(" ".join(list(map(lambda x : str(x) ,basket))))