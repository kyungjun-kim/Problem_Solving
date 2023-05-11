#문제 링크 : https://www.acmicpc.net/problem/2444
ran = int(input())
cnt = 1
for i in range(1,(ran*2)):
    if i < ran :
        print("{}{}".format(" " * (ran-i) , "*"*cnt," " * (ran-(4*i))))
        cnt += 2    
    else :
        print("{}{}".format(" " * (i-ran) , "*"*cnt," " * (ran-(4*i))))
        cnt -= 2
    