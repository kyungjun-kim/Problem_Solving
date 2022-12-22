# 문제 링크 : https://www.acmicpc.net/problem/2908

A, B = map(str, input().split())
ans_1,ans_2 = [],[]
for i in range(2,-1,-1):
    ans_1.append(str(A[i]))
    ans_2.append(str(B[i]))
if ans_1 < ans_2:
    print(int(''.join(ans_2)))
elif ans_1 > ans_2:
    print(int(''.join(ans_1)))