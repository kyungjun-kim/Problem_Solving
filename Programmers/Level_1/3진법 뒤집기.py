def solution(n):
    def numeral_system(number, base):
        NOTATION = '0123456789ABCDEF'
        q, r = divmod(number, base)
        n = NOTATION[r]
        return numeral_system(q, base) + n if q else n
    return int(numeral_system(n, 3)[::-1], 3)