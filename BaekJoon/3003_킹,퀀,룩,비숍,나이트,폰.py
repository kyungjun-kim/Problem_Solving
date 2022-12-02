# 문제 링크 : https://www.acmicpc.net/problem/3003

og = [1, 1, 2, 2, 2, 8]
answer = list(map(lambda x : int(x), input().split()))
print(' '.join(list(map(lambda x,y : str(x-y), og,answer))))