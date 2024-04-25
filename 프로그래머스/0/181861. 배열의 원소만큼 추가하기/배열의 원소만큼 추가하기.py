def solution(arr):
    return list(map(int,"".join([(str(x)+" ") * x for x in arr]).split(" ")[:-1]))