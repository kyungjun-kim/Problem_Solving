def solution(s):
    return "".join(sorted(list(filter(lambda f : s.count(f) == 1, s))))