# 문제링크 : https://www.acmicpc.net/problem/2798

from itertools import combinations
N,M = list(map(lambda x : int(x), input().split()))
c_cnt = (list(map(lambda x : int(x), input().split())))
print(max(list(filter(lambda f : f<=M ,map(lambda x : sum(list(x)), combinations(c_cnt,3))))))