def solution(data, ext, val_ext, sort_by):
    check = ["code", "date", "maximum","remain"]
    answer = list(filter(lambda x : x[check.index(ext)] < val_ext, data))
    answer = sorted(answer, key = lambda x : x[check.index(sort_by)])
    return answer