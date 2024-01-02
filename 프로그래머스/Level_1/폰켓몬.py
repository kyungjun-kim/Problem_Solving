def solution(nums):
    answer = len(nums)/2
    n = list(set(nums))
    if answer > len(n) :
        return len(n)
    else :
        return answer