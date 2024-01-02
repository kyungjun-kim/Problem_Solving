def solution(sizes):
    """w = 1
    h = 1
    for i in sizes :
        i.sort()
        if i[0] > w :
            w = i[0]
        if i[1] > h :
            h = i[1]"""
    return max(min(x) for x in sizes) * max(max(x) for x in sizes)