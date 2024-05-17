def solution(arr):
    answer = 0
    while True :
        tmp = arr.copy()
        arr = list(map(lambda x : x//2 if x >= 50 and x % 2 == 0 else x * 2 + 1 if x < 50 and x % 2 else x ,arr))
        if arr == tmp :
            return answer
        answer += 1