#문제 링크 : https://www.acmicpc.net/problem/25206
score = []
s_sum = 0
s_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0 ,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F" :0.0}
for i in range(20) :
    inp = input().split()
    if inp[2] != "P" :
        score.append(float(inp[1]) * s_dict[inp[2]])
        s_sum += float(inp[1])
print(sum(score)/s_sum)