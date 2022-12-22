# 문제링크 : https://www.acmicpc.net/problem/1181

result = []
for i in range(int(input())) :
    result.append(input())
for i in sorted(list(set(result)) , key=lambda k : [len(k),k]) :
    print(i)