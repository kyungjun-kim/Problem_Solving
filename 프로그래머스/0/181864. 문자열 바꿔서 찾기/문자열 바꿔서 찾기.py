def solution(myString, pat):
    return int(pat in "".join(["A" if x == "B" else "B" for x in myString]))