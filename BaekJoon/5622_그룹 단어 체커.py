# 문제 링크 : https://www.acmicpc.net/problem/5622

num = int(input())
answer = 0
words,tmp = [],[]
for i in range(num) :
    words.append(input())
for i in words :
    tmp = []
    answer += 1
    for j in i :
        if len(tmp) > 0 and j != tmp[-1] and j in tmp :
            answer -= 1
            break
        else :
            tmp.append(j)
print(answer)