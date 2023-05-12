#문제 링크 : https://www.acmicpc.net/problem/1271

n,m = map(lambda x : int(x) , input().split())
print("{}\n{}".format(n//m,n%m))