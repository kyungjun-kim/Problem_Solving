def solution(q, r, code):
    return ''.join([y if x % q == r else '' for x,y in enumerate(code)])