#문제 링크 : https://www.acmicpc.net/problem/10811

N,M = list(map(lambda x : int(x), input().split()))
basket = list(map(lambda x : x, range(1,N+1)))
for r in range(M) :
    i,j = list(map(lambda x : int(x)-1, input().split()))
    basket = basket[:i] + basket[i:j+1][::-1] + basket[j+1:]
print(" ".join(list(map(lambda x : str(x) ,basket))))