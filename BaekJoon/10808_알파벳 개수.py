#문제 링크 : https://www.acmicpc.net/problem/10808

string = input()
print(' '.join(list(map(lambda x : str(string.count(chr(x))) , range(97,123)))))