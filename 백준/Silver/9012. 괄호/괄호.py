N = int(input())
for i in range(N) :
    a = input()
    while True :
        if a.count("(") != a.count(")") or a[0] == ")" or a[-1] == "(":
            print("NO")
            break
        if a == "()" or "" :
            print("YES")
            break
        a = a.replace("()",'',1)