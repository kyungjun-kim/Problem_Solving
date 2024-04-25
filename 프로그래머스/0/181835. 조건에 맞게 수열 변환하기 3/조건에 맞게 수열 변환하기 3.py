def solution(arr, k):
    return [x*k if k%2 else x+k for x in arr]