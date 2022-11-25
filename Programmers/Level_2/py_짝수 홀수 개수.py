# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    a = list(filter(lambda x : x % 2 == 0, num_list))
    b = list(filter(lambda x : x % 2 != 0, num_list))
    return [len(a),len(b)]