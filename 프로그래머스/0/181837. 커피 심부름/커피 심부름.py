def solution(order):
    return sum(list(map(lambda x : 5000 if "latte" in x else 4500 , order)))