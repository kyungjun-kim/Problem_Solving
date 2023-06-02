#문제 링크 : https://www.acmicpc.net/problem/1085
x, y, w, h = list(map(lambda x : int(x) , input().split()))
print(min(h-y, y-0, w-x,x-0))