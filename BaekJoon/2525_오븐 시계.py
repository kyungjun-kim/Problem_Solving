# 문제 링크 : https://www.acmicpc.net/problem/2525

import datetime as dt
a = input()
b = int(input())
answer = dt.datetime.strptime(a, '%H %M') + dt.timedelta(minutes=b)
print("{} {}".format(answer.hour, answer.minute))