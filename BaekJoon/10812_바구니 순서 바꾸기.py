#문제링크 : https://www.acmicpc.net/problem/10812

N,M = list(map(lambda x : int(x), input().split()))
basket = list(map(lambda x : x, range(1,N+1)))
for i in range(M) :
    i,j,k = list(map(lambda x : int(x)-1, input().split()))
    basket = basket[:i] + basket[k:j+1] + basket[i:k] + basket[j+1:]
print(" ".join(list(map(lambda x : str(x) ,basket))))
