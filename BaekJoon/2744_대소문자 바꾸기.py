#문제 링크 : https://www.acmicpc.net/problem/2744
s = input()
answer = ''
for i in s :
    if ord(i) >= 97 :
        answer += chr(ord(i)-32)
    else :
        answer += chr(ord(i)+32)
print(answer)