# 문제풀이 : https://www.acmicpc.net/status?user_id=kkj214&problem_id=4153&from_mine=1

while True :
    result = sorted(list(map(lambda x : int(x) , input().split())))
    if result[-1] == 0 :
        break
    if result[0]**2 + result[1]**2 == result[2] ** 2 :
        print("right")
    else :
        print("wrong")
