# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True 

def solution(nums):
    result = list(map(lambda x : sum(list(x)) ,combinations(nums, 3)))
    answer = len(list(filter(lambda x : is_prime_number(x) == True, result)))
    return answer