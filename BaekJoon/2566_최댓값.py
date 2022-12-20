# 문제링크 : https://www.acmicpc.net/submit/2566

result = []
for i in range(9) :
    tmp = list(map(lambda x : int(x), input().split()))
    result.append(tmp)
result = sum(result,[])
print(max(result))
print(result.index(max(result))//9 + 1, result.index(max(result)) % 9 + 1)
