def solution(A, B):
    cnt = 0
    for i in range(len(A)) :
        if A == B :
            return cnt
        cnt += 1
        A = A[-1] + A[:-1]
    return -1