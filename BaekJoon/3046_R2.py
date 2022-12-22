#문제 링크 : https://www.acmicpc.net/problem/3046

answer = list(map(lambda x : int(x), input().split()))
print(answer[1]*2 - answer[0])