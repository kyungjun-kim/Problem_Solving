def solution(arr):
    return list(map(lambda x : x / 2 if x >= 50 and x % 2==0 else x * 2 if x < 50 and x % 2 else x, arr))