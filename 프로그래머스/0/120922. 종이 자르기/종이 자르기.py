def solution(M, N):
    answer = (min(M,N) * (max(M,N) - 1)) + min(M,N) - 1
    return answer