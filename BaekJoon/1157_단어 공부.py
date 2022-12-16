# 문제 링크 : https://www.acmicpc.net/problem/1157

a = input().upper()
if len(a) == 1 :
    print(a.upper())
else:
    result = sorted(list(map(lambda x : [a.count(x),x] , list(set(a)))), reverse= True)
    if result[0][0] == result[1][0] :
        print("?")
    else :
        print(result[0][1])