def solution(before, after):
    b = sorted(list(before))
    a = sorted(list(after))
    if a == b :
        return 1
    else :
        return 0