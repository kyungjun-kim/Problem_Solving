# 문제 링크 : https://www.acmicpc.net/source/60610399
inp = int(input())
if inp % 4 == 0 :
    print("{}int".format("long "* (inp // 4)))
else :
    print("{}int".format("long "* ((inp // 4)+1)))
